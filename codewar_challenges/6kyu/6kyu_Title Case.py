def title_case(title, minor_words=''):
    if title=='' or title==' ':
        return ''
    title_list = [n.lower() for n in title.split(' ')]
    minor_words_list = [n.lower() for n in minor_words.split(' ')]
    out_put_list = " ".join([n[0].upper()+n[1:] if n not in minor_words_list else n for n in title_list])
    return (out_put_list[0].upper()+out_put_list[1:])
title_case('a clash of KINGS', 'a an the of')


def title_case(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() for word in title])