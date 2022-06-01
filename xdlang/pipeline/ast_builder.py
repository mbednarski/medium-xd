from typing import Any

from lark import Token, Transformer

import xdlang.pipeline.nodes as xdnodes


class AstBuilder(Transformer):
    def LITERAL(self, item: Token) -> xdnodes.LiteralExprNode:
        return xdnodes.LiteralExprNode(item.line, item.column, int(item.value))

    def expr(self, items: list[Any]) -> xdnodes.ExprNode:
        return items[0]

    def return_stmt(self, items: list[Any]) -> xdnodes.ReturnStmtNode:
        expr = items[1]
        return xdnodes.ReturnStmtNode(expr.line, expr.column, expr)

    def block(self, items: list[Any]) -> xdnodes.BlockNode:
        statements = items[1:-1]
        return xdnodes.BlockNode(items[0].line, items[0].column, statements)

    def func_def(self, items: list[Any]) -> xdnodes.FuncDefNode:
        type = items[0].value
        identifier = items[1].value
        body = items[2]
        return xdnodes.FuncDefNode(
            items[0].line, items[0].column, type, identifier, body
        )

    def program(self, items: list[Any]) -> xdnodes.ProgramNode:
        return xdnodes.ProgramNode(0, 0, items)
