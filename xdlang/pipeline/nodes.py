import abc


class Node(abc.ABC):
    def __init__(self, line: int, column: int) -> None:
        self.line = line
        self.column = column


class ExprNode(Node):
    def __init__(self, line: int, column: int) -> None:
        super().__init__(line, column)


class StmtNode(Node):
    def __init__(self, line: int, column: int) -> None:
        super().__init__(line, column)


class LiteralExprNode(ExprNode):
    def __init__(self, line: int, column: int, value: int) -> None:
        super().__init__(line, column)
        self.value = value


class ReturnStmtNode(StmtNode):
    def __init__(self, line: int, column: int, expr: ExprNode) -> None:
        super().__init__(line, column)
        assert isinstance(expr, ExprNode)
        self.expr = expr


class BlockNode(Node):
    def __init__(self, line: int, column: int, stmts: list[StmtNode]) -> None:
        super().__init__(line, column)
        assert all([isinstance(n, StmtNode) for n in stmts])
        self.stmts = stmts


class FuncDefNode(Node):
    def __init__(
        self, line: int, column: int, type: str, identifier: str, body: BlockNode
    ) -> None:
        super().__init__(line, column)
        self.type = type
        self.identifier = identifier
        assert isinstance(body, BlockNode)
        self.body = body


class ProgramNode(Node):
    def __init__(self, line: int, column: int, func_defs: list[FuncDefNode]) -> None:
        super().__init__(line, column)
        assert all([isinstance(n, FuncDefNode) for n in func_defs])
        self.func_defs = func_defs
