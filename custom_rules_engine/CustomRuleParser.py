from rule_engine import parser, ast

from custom_rules_engine.CustomRuleExpressions import NVLResolutionExpression

class CustomRuleParser(parser.Parser):
    customTokens = ("NVL",)

    # It could be a attribute (t_NVL = r'NVL') or a function as mentioned below.
    def t_NVL(self, t):
        r'NVL'
        return t

    def p_expression_NVL(self,p):
        'expression : NVL expression'
        p[0] = p[2]

    def p_expression_decode(self,p):
        '''expression : expression COMMA expression
        '''
        left, op, right, replacement = p[1], "==", ast.NullExpression(self.context), p[3]
        op_name = self.op_names[op]
        p[0] = NVLResolutionExpression(self.context, op_name, left, right,replacement).reduce()

    tokens = parser.Parser.tokens + customTokens