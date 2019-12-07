def check_case(result):
    if( 0 in result):
        return 'wrong'
    else:
        return 'correct'
def check_test_case(answer, result):
    if(check_case(result)=='wrong' and answer=='wrong'):
        return 'fine'
    elif(check_case(result)=='correct' and answer=='wrong'):
        return 'invalid'
    elif(check_case(result)=='wrong' and answer=='correct'):
        return 'weak'
    elif(check_case(result)=='correct' and answer=='correct'):
        return 'fine'

cases = int(input(""))
for case in range(cases):
    n,m = map(int, input("").split(" "))

    case_results = []
    for test_case in range(n):
        answer, result = map(str, input("").split(" "))
        result = list(map(int, list(result)))
        case_results.append(check_test_case(answer, result))
    if 'invalid' in case_results:
        print("INVALID")
    elif 'weak' in case_results:
        print('WEAK')
    else:
        print('FINE')