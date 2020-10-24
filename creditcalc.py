
import argparse
import math
import sys

if len(sys.argv) == 5:
    CLI = argparse.ArgumentParser()
    CLI.add_argument("--type", choices=['diff', 'annuity'])
    CLI.add_argument("--principal", help='principal of loan', type=float)
    CLI.add_argument("--payment", help='number of payments', type=float)
    CLI.add_argument("--periods", help='number of periods, must be positive', type=int)
    CLI.add_argument("--interest", help='interest on loan', type=float)
    args = CLI.parse_args()

    if args.type == "diff" and args.periods and args.principal and args.interest:
        i = float(args.interest / 100) / (12 * (100 / 100))
        total = 0
        month = 1
        while month <= args.periods:
            d = (args.principal / args.periods) + i * (args.principal - (args.principal * (month - 1) / args.periods))
            print(f'Month {month}: payment is {math.ceil(d)}')
            total += math.ceil(d)
            month += 1
        else:
            over = total - math.ceil(args.principal)
            print(f'Overpayment = {over}')
            exit()

    elif args.type == "annuity" and args.periods and args.principal and args.interest:
        i = float(args.interest / 100) / (12 * (100 / 100))
        payment = args.principal * ((i * math.pow(1 + i, args.periods)) / (math.pow(1 + i, args.periods) - 1))
        print(f'Your annuity payment = {math.ceil(payment)}!')
        overpay = (math.ceil(payment) * args.periods) - args.principal
        print(f'Overpayment = {int(overpay)}')

    elif args.payment and args.periods and args.interest is not None:
        i = float(args.interest / 100) / (12 * (100 / 100))
        loan_principal = args.payment / ((i * math.pow(1 + i, args.periods)) / (math.pow(1 + i, args.periods) - 1))
        print(f'Your loan principal = {math.floor(loan_principal)}!')
        overpay = (math.ceil(args.payment) * args.periods) - loan_principal
        print(f'Overpayment = {math.ceil(overpay)}')

    elif args.type == "annuity" and args.principal is not None and args.payment is not None and args.interest \
            is not None:
        i = float(args.interest / 100) / (12 * (100 / 100))
        n = math.log(args.payment / (args.payment - i * args.principal), i + 1)
        year, month = divmod(n, 12)
        if 11 < month < 12:
            year += 1
            month = 0
            print(f'It will take {int(year)} years and {math.ceil(month)} months to repay this loan!')
        else:
            print(f'It will take {int(year)} years and {math.ceil(month)} months to repay this loan!')
        overpay = (args.payment * math.ceil(n)) - args.principal
        print(f'Overpayment = {int(overpay)}')

    elif args.type == 'diff' and args.payment:
        print('Incorrect parameters')
        sys.exit()
else:
    print('Incorrect parameters')
    sys.exit()
