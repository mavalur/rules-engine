from rule_engine import Rule, Context
from custom_rules_engine.CustomRuleParser import CustomRuleParser

class CustomRuleEngine(Rule):
    Rule.parser = CustomRuleParser()

# Handling null cases, with object manipulation
condition = "BOOK_PRICE == null"
#condition = "NVL(BOOK_PRICE,66)"

# Handling null cases with computation
#condition = "(BOOK_PRICE * 2) == 200"
#condition = "NVL(BOOK_PRICE,66) * 2  >150"

customContext = Context(default_value=None)
re = CustomRuleEngine(text=condition, context=customContext)

facts = [{
    "BOOK_ID":1,
    "BOOK_PRICE":100
},{
    "BOOK_ID":2,
    "BOOK_PRICE":None
},{
    "BOOK_ID":3
}]

results = re.filter(facts)

for r in results:
    print(r)