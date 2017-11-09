import operator
from types import LambdaType
import tinybit_errors
import contextos
from tinybit_errors import *
import numpy as np
import pprint
context = contextos.SymbolTable()

class InstructionList:
    def __init__(self, children=None):
        if children is None:
            children = []
        self.children = children

    def __len__(self):
        return len(self.children)

    def __iter__(self):
        return iter(self.children)

    def __repr__(self):
        return '<InstructionList {0}>'.format(self.children)

    def eval(self):
        """
        Evaluates all the class children and returns the result
        of their eval method in a list or returns an ExitStatement
        in case one is found
        """

        ret = []
        for n in self:
            if isinstance(n, ExitStatement):
                return n

            res = n.eval()

            if isinstance(res, ExitStatement):
                return res
            elif res is not None:
                ret.append(res)

        return ret


class BaseExpression:
    def eval(self):
        raise NotImplementedError()


class ExitStatement(BaseExpression):
    def __iter__(self):
        return []

    def eval(self):
        pass


def full_eval(expr: BaseExpression):
    """
    Fully evaluates the passex expression returning it's value
    """

    while isinstance(expr, BaseExpression):
        expr = expr.eval()

    return expr


class Primitive(BaseExpression):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return '<Primitive "{0}"({1})>'.format(self.value, self.value.__class__)

    def eval(self):
        return self.value


class Identifier(BaseExpression):
    is_function = False

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Identifier {0}>'.format(self.name)

    def assign(self, val):
        if self.is_function:
            context.set_func(self.name, val)
        else:
            context.set_sym(self.name, val)

    def eval(self):
        if self.is_function:
            return context.get_func(self.name)
        return context.get_sym(self.name)


class Array(BaseExpression):
    def __init__(self, values: InstructionList):
        self.values = values

    def __repr__(self):
        return '<Array len={0} items={1}>'.format(len(self.values.children), self.values)

    def eval(self):
        return self.values.eval()

class ArrayInit(BaseExpression):
    def __init__(self, array: Identifier, dimensionx: Primitive, dimensiony = None):
        self.dimensionx = dimensionx
        self.dimensiony = dimensiony
        self.array = array

    def eval(self):
        array_data = []
        aux = []
        for x in range(0,self.dimensionx):
            for y in range(0,self.dimensiony):
                aux.append(Primitive(0))
            array_data.append(aux)
            aux = []
        return self.array.assign(array_data)


class ArrayAccess(BaseExpression):
    def __init__(self, array: Identifier, index1: BaseExpression, index2 = None):
        self.array = array
        self.index1 = index1
        self.index2 = index2        

    def __repr__(self):
        if self.index2 is not None:
            return '<Array index1={0} index2={1}>'.format(self.index1.eval(), self.index2.eval())
        return '<Array index={0}>'.format(self.index1)

    def eval(self):
        if self.index2 is not None:
            return self.array.eval()[self.index1.eval()][self.index2.eval()].eval()  
        return self.array.eval()[self.index1.eval()]

class InputStatement(BaseExpression):
    def __init__(self, Identifier: Identifier):
        self.Identifier = Identifier
    
    def eval(self):
        indata = input()
        self.Identifier.assign(indata)

class ArrayAssign(BaseExpression):
    def __init__(self, array: Identifier, index: BaseExpression, value: BaseExpression, index2 = None):
        self.array = array
        self.index = index
        self.value = value
        self. index2 = index2
        
    def __repr__(self):
        return '<Array arr={0} index={1} value={2}>'.format(self.array, self.index, self.value)

    def eval(self):
        if self.index2 is not None:
            self.array.eval()[self.index.eval()][self.index2.eval()] = Primitive(self.value.eval())
        else:
            self.array.eval()[self.index.eval()] = self.value.eval()


class ArraySlice(BaseExpression):
    def __init__(self, array: Identifier, start: BaseExpression=None, end: BaseExpression=None):
        self.array = array
        self.start = start
        self.end = end

    def __repr__(self):
        return '<ArraySlice array={0} start={1} end={2}>'.format(self.array, self.start, self.end)

    def eval(self):
        if self.start is not None and self.end is not None:
            # access [start : end]
            return self.array.eval()[self.start.eval():self.end.eval()]

        elif self.start is None and self.end is not None:
            # access [: end]
            return self.array.eval()[:self.end.eval()]

        elif self.start is not None and self.end is None:
            # access [start :]
            return self.array.eval()[self.start.eval():]
        else:
            return self.array.eval()[:]


class Assignment(BaseExpression):
    def __init__(self, identifier: Identifier, val):
        self.identifier = identifier
        self.val = val

    def __repr__(self):
        return '<Assignment sym={0}; val={1}>'.format(self.identifier, self.val)

    def eval(self):
        if self.identifier.is_function:
            self.identifier.assign(self.val)
        else:
            self.identifier.assign(self.val.eval())


class BinaryOperation(BaseExpression):
    __operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '**': operator.pow,
        '/': operator.truediv,
        '%': operator.mod,

        '>': operator.gt,
        '>=': operator.ge,
        '<': operator.lt,
        '<=': operator.le,
        '==': operator.eq,
        '!=': operator.ne,

        'and': lambda a, b: a.eval() and b.eval,
        'or': lambda a, b: a.eval() or b.eval(),

        '&': operator.and_,
        '|': operator.or_,
        '^': operator.xor,
        '>>': operator.rshift,
        '<<': operator.lshift,
    }

    def __repr__(self):
        return '<BinaryOperation left ={0} right={1} operation="{2}">'.format(self.left, self.right, self.op)
        
    def __init__(self, left, right, op):
        self.left = left
        self.right = right
        self.op = op

    def eval(self):
        left = None
        right = None

        try:
            # find the operation that needs to be performed
            op = self.__operations[self.op]
            # The only lambda operations are logical and/or
            # Pass the arguments unevaluated as they will be during the lambda execution
            # This implements short circuit boolean evaluation
            if isinstance(op, LambdaType):
                return op(self.left, self.right)

            # otherwise, straight up call the operation, also save the variables
            # in case they are to be used for the exception block
            left = self.left.eval()
            right = self.right.eval()
            print(f"{self.op} {left} {right} {op(left,right)}")
            return op(left, right)
        except TypeError:
            fmt = (left.__class__.__name__, left, self.op, right.__class__.__name__, right)


class CompoundOperation(BaseExpression):
    __operations = {
        '+=': operator.iadd,
        '-=': operator.isub,
        '/=': operator.itruediv,
        '*=': operator.imul,
        '%=': operator.imod,
        '**=': operator.ipow,
    }

    def __init__(self, identifier: Identifier, modifier: BaseExpression, operation: str):
        self.identifier = identifier
        self.modifier = modifier
        self.operation = operation

    def __repr__(self):
        fmt = '<Compound identifier={0} mod={1} operation={2}>'
        return fmt.format(self.identifier, self.modifier, self.operation)

    def eval(self):
        # Express the compound operation as a 'simplified' binary op
        # does not return anything as compound operations
        # are statements and not expressions

        l = self.identifier.eval()
        r = self.modifier.eval()

        try:
            self.identifier.assign(self.__operations[self.operation](l, r))
        except TypeError:
            fmt = (l.__class__.__name__, l, self.operation, r.__class__.__name__, r)
            raise InterpreterRuntimeError("Unable to apply operation (%s: %s) %s (%s: %s)" % fmt)


class UnaryOperation(BaseExpression):
    __operations = {
        '+': operator.pos,
        '-': operator.neg,
        '~': operator.inv,
        'not': operator.not_
    }

    def __repr__(self):
        return '<Unary operation: operation={0} expr={1}>'.format(self.operation, self.expr)

    def __init__(self, operation, expr: BaseExpression):
        self.operation = operation
        self.expr = expr

    def eval(self):
        return self.__operations[self.operation](self.expr.eval())


class If(BaseExpression):
    def __init__(self, condition: BaseExpression, truepart: InstructionList, elsepart=None):
        self.condition = condition
        self.truepart = truepart
        self.elsepart = elsepart
    def __repr__(self):
        return '<If condition={0} then={1} else={2}>'.format(self.condition, self.truepart, self.elsepart)

    def eval(self):
        if self.condition.eval():
            print("GOTO TRUEPART")            
            if isinstance(self.truepart, str):
                return self.truepart
            else:
                return self.truepart.eval()
        elif self.elsepart is not None:
            print("GOTO FALSEPART")            
            return self.elsepart.eval()
        else:
            print("GOTO SKIP")


class For(BaseExpression):
    def __init__(self, variable: Identifier, start: Primitive, end: Primitive, asc: bool, body: InstructionList):
        self.variable = variable
        self.start = start
        self.end = end
        self.asc = asc  # ascending order
        self.body = body

    def __repr__(self):
        fmt = '<For start={0} direction={1} end={2} body={3}>'
        return fmt.format(self.start, 'asc' if self.asc else 'desc', self.end, self.body)

    def eval(self):
        if self.asc:
            lo = self.start.eval()
            hi = self.end.eval() + 1
            sign = 1
        else:
            lo = self.start.eval()
            hi = self.end.eval() - 1
            sign = -1
        for i in range(lo, hi, sign):
            self.variable.assign(i)
            if sign == 1:   
                a = i + 1
                print(f"<= {i} {hi-1} {i<hi}")
                print(f"+ {self.variable} {1} {a}")
            if sign == -1:
                a = i - 1                
                print(f">= count {i} {hi-1} {i>=hi}")
                print(f"- {self.variable} {i} {1} {a}")                          
            print("GOTO START")
                # in case of exit statement prematurely break the loop
            if isinstance(self.body.eval(), ExitStatement):
                break
        print("GOTO END")


class ForIn(BaseExpression):
    def __init__(self, variable: Identifier, sequence: BaseExpression, body: InstructionList):
        self.variable = variable
        self.sequence = sequence
        self.body = body

    def __repr__(self):
        return '<ForIn var={0} in iterable={1} do body={2}>'.format(self.variable, self.sequence, self.body)

    def eval(self):
        for i in self.sequence.eval():
            self.variable.assign(i)
            if isinstance(self.body.eval(), ExitStatement):
                break


class While(BaseExpression):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def __repr__(self):
        return '<While cond={0} body={1}>'.format(self.condition, self.body)

    def eval(self):
        print("GOTO F BREAK")
        while self.condition.eval():
            if isinstance(self.body.eval(), ExitStatement):
                break


class PrintStatement(BaseExpression):
    def __init__(self, items: InstructionList):
        self.items = items

    def __repr__(self):
        return '<Print {0}>'.format(self.items)

    def eval(self):
        if not isinstance(*self.items.eval(),list):
            print(*self.items.eval(), end='', sep='')
        else:
            tupple = self.items.eval()
            aux = []
            array = []
            for x in tupple[0]:
                for y in x:
                    aux.append(y.eval())
                array.append(aux)
                aux = []
            print(array)

class FunctionCall(BaseExpression):
    def __init__(self, name: Identifier, params: InstructionList):
        self.name = name

    def __repr__(self):
        return '<Function call name={0} params={1}>'.format(self.name, self.params)

    def __eval_builtin_func(self):
        func = self.name.eval()


        return func.eval()

    def __eval_udf(self):
        func = self.name.eval()
        # pair the defined parameters in the function signature with
        # whatever is being passed on.
        #
        # On the parameters we only need the name rather than fully evaluating them

        return func.eval()

    def eval(self):
        if isinstance(self.name.eval(), BuiltInFunction):
            return self.__eval_builtin_func()

        return self.__eval_udf()


class Function(BaseExpression):
    def __init__(self, params: InstructionList, body: InstructionList):
        self.params = params
        self.body = body

    def __repr__(self):
        return '<Function params={0} body={1}>'.format(self.params, self.body)

    def eval(self):
        context.set_local(True)

        try:
            ret = self.body.eval()

        finally:
            context.set_local(False)

        return None


class BuiltInFunction(BaseExpression):
    def __init__(self, func):
        self.func = func

    def __repr__(self):
        return '<Builtin function {0}>'.format(self.func)

    def eval(self, args):
        return self.func(*args)


class InExpression(BaseExpression):
    def __init__(self, a: BaseExpression, b: BaseExpression, not_in: bool=False):
        self.a = a
        self.b = b
        self.not_in = not_in

    def __repr__(self):
        return '<In {0} in {1}>'.format(self.a, self.b)

    def eval(self):
        if self.not_in:
            return self.a.eval() not in self.b.eval()
        return self.a.eval() in self.b.eval()


class TernaryOperator(BaseExpression):
    def __init__(self, cond: BaseExpression, trueval: BaseExpression, falseval: BaseExpression):
        self.cond = cond
        self.trueval = trueval
        self.falseval = falseval

    def __repr__(self):
        return '<Ternary cond={0} true={1} false={2}>'.format(self.cond, self.trueval, self.falseval)

    def eval(self):
        return self.trueval.eval() if self.cond.eval() else self.falseval.eval()