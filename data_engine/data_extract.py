from .yahoo_finance import get_data


def data_extract(args):
    args_dict = vars(args)
    if args_dict['broker'] == 'yf':
        data = get_data(args)
        return data