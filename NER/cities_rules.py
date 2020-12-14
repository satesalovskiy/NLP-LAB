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
    NAME = gram('Name')
    PREP=gram('PREP')
    #GEO=gram('Geox') 
    GEO=rule ( and_(
    gram('Geox'),
    not_(or_(
        eq('артема'),
        eq('фармана'),
        eq('оскол'),
        eq('мунарева'),
    ))
    )
    )


    NAME_OR_NOUN = or_(
        NAME,
        NOUN
    )

    CITY = morph_pipeline([ 
        'город', 
        'Нижний', 
        'новгород' 
    ])

    CITY_EXEP=rule(morph_pipeline([
        'артем',
        'фармана',
        'оскол'
        
    ]))

    CITY_NOT=rule(
        not_(  or_(
        eq('артем'),
        eq('фармана'),
        eq('оскол'),
        INT
        ))
    )


    COMPLICATED_CITY = or_(
            rule(
                CITY.optional(),
                GEO
        )
    )

    FINAL_CITY = or_(COMPLICATED_CITY)
    return FINAL_CITY

