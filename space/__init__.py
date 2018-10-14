from decimal import Context
from decimal import ROUND_HALF_DOWN
from decimal import setcontext


setcontext(Context(prec=4, rounding=ROUND_HALF_DOWN))
