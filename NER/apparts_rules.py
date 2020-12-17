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
    CONJ=gram('CONJ')
    NAME = gram('Name')
    PREP=gram('PREP')
    NPRO=gram('NPRO')
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

    HOUSE=morph_pipeline([
        'дом',
        'корпус',
        'квартира',
        'строение',
        'ст'
    ])

    CITY_EXEP=rule(morph_pipeline([
        'артем',
        'фармана',
        'оскол'
        
    ]))

    HOUSE_NOT=rule( 
        and_(  
            not_(ADJF) 
        ) 
    )
    HOUSE1=morph_pipeline([ 
        'a', 
        'а', 
        '/', 
        'б' 
    ])

    UNIT1=or_( 
        rule( 
            and_(INT,not_(eq('3'))), 
            HOUSE1.optional(), 
            HOUSE_NOT.optional(), 
            INT.optional() 
        )
    )

    DOUBLED = rule(
        RU,
        RU
    )

    UNIT = or_(
            rule(
                HOUSE.optional(),
                UNIT1
        )
    )

    COMPLICATED_HOUSE=rule(
        UNIT.repeatable()
    )



    FINAL_HOUSE = or_(COMPLICATED_HOUSE)
    return FINAL_HOUSE
