################################################################################
# NVL Resolution expression
################################################################################
from rule_engine.ast import ComparisonExpression

class NVLResolutionExpression(ComparisonExpression):
    """NVL Type literal expressions, that evaluates to a boolean match first, (if the value is none)
    Followed by a symbol resolution or replacement. Thing is also enhanced as part of rule filtering."""
    def __init__(self, context,op_name, left, right, replacement):
        super(ComparisonExpression,self).__init__(context, op_name, left, right)
        self._replacement = replacement
        self._left = left
        self.result_type = self._replacement.result_type

    def evaluate(self, thing):
         isNone = self._evaluator(thing)
         if not isNone:
             return_value = self._left.evaluate(thing)
         else:
            return_value = self._replacement.value
            thing[self._left.name] = return_value
         return  return_value

