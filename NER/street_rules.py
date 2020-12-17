from yargy import Parser, rule, and_, not_, or_
from yargy.interpretation import fact
from yargy.predicates import gram
from yargy.predicates import eq, type
from yargy.relations import gnc_relation
from yargy.pipelines import morph_pipeline
from random import seed, sample
from ipymarkup import show_ascii_markup
from ipymarkup import show_box_markup
from yargy.tokenizer import MorphTokenizer

def get_rules():
    RU = type('RU')
    INT = type('INT')
    NONE = type('NONE')
    NOUN= gram('NOUN')
    ADJF = gram('ADJF')
    GEO = gram('Geox')
    PREP = gram('PREP')
    CONJ = gram('CONJ')

    NAME = rule ( and_(
            gram('Name'),
            not_(PREP),
            not_(GEO)
        )
    )
    
    
    NOUN_NOT_CONJ = rule ( and_(
        NOUN,
        not_(CONJ)
        )
    )   

    STREET_SUFFIXS = morph_pipeline([
        'улица',
        'тракт',
        'бульвар',
        'проспект',
        'микрорайон',
        'проезд',
        'шоссе',
        'парк'
    ])

    SPECIAL_STREET_SUFFIXS = morph_pipeline([
        'шоссе',
        'тракт'
    ])

    SIMPLE_STREETS_FROM_ARRAY = morph_pipeline([
        'краснопресненская',
        'республике',
        'маршала захарова',
        'доватора',
        'мичурина',
        'зеленые аллеи',
        'бехтеева',
        'октябрьская',
        'новогиреевская',
        'югорская',
        'артема',
        'парковая',
        'зеленые аллеи',
        'алтуфьевское',
        'горького',
        'Кавказский',
        'хамовнический вал',
        'Кусковская',
        'марьинский парк',
        'московская',
        'береговая',
        'антонова овсиенко',
        'школьная',
        'юнтоловский',
        'гагарина'

    ])

    EXCEPTIONAL_STREET_CONST = morph_pipeline([
        'Кавказский'
    ])

    NOUN_NOT_APPART = rule(
        not_(  or_(
            eq('дом'),
            eq('квартира'),
            INT,
            CONJ
        ))
    )

    COMPLICATED_STREETS = or_(
            rule(
                STREET_SUFFIXS,
                INT,
                NOUN,
                NOUN
        ),
            rule(
                STREET_SUFFIXS,
                INT,
                ADJF,
                NOUN
        ),
            rule(
                STREET_SUFFIXS,
                NOUN_NOT_CONJ,
                NOUN_NOT_APPART,
                NAME.optional()
        ),
            rule(
                NAME,
                NOUN_NOT_APPART
        ),
            rule(
                ADJF,
                NAME
        ),
            rule(
                STREET_SUFFIXS,
                ADJF,
                NOUN_NOT_APPART
        ),
            rule(
                STREET_SUFFIXS,
                CONJ,
                NOUN,
                NOUN  
        )
    )

    SIMPLE_STREETS_WITH_STREET_SUFFIX = rule(
        STREET_SUFFIXS,
        NOUN_NOT_APPART
    )
    SPECIAL_SIMPLE_STREETS_WITH_STREET_SUFFIX = rule (
        ADJF,
        SPECIAL_STREET_SUFFIXS
    )

    SIMPLE_STREETS = or_(
        SPECIAL_SIMPLE_STREETS_WITH_STREET_SUFFIX,
        SIMPLE_STREETS_WITH_STREET_SUFFIX,
        SIMPLE_STREETS_FROM_ARRAY
    )

    FINAL_STREET = or_(COMPLICATED_STREETS, SIMPLE_STREETS)

    return FINAL_STREET

