from random import shuffle

poomsae_list = {
    1: ['il jang', '일 장', 18],
    2: ['ee jang', '이 장', 18],
    3: ['sam jang', '삼 장', 20],
    4: ['sah jang','사 장', 20],
    5: ['oh jang', '오 장', 20],
    6: ['yuk jang', '육 장', 19],
    7: ['chil jang', '칠 장', 25],
    8: ['pal jang','팔 장', 27],
    9: ['koryo','코료', 30],
    10: ['geumgang','금강', 27],
    11: ['taebaek', '태백', 26],
    12: ['pyongwon','평원',21],
    13: ['sipjin','싶진', 28],
    14: ['jitae', '지태', 28],
    15: ['chonkwon','촌권',26],
    16: ['hansu','한수',27],
    17: ['ilyeo','일여',23],
}


def random_poomsae_list(max_p=8):
    p = list(range(1, max_p+1))
    selected = list()
    shuffle(p)
    for x in p:
        selected.append(poomsae_list.get(x))

    return selected
