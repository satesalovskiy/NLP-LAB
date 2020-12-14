from yargy import Parser, rule, and_, not_, or_
from yargy.interpretation import fact
from yargy.predicates import gram,normalized, caseless,in_caseless,in_,length_eq
from yargy.predicates import eq, type
from yargy.relations import gnc_relation
from yargy.pipelines import morph_pipeline
from random import seed, sample
from ipymarkup import show_ascii_markup
from ipymarkup import show_box_markup
from yargy.tokenizer import MorphTokenizer
from yargy.tokenizer import QUOTES

def get_mid_rules():
    RU = type('RU')
    INT = type('INT')
    NONE = type('NONE')
    NOUN= gram('NOUN')
    ADJF = gram('ADJF')
    CONJ=gram('CONJ')
    PATR=gram('Patr')
    NAME = gram('Name')
    PREP=gram('PREP')

    PATRONYMIC=rule(
        PATR
    )

    COMPLICATED=rule(
        PATRONYMIC.repeatable()
    )

    FINAL = or_(COMPLICATED)
    return FINAL

def get_first_rules():
    RU = type('RU')
    INT = type('INT')
    NONE = type('NONE')
    NOUN= gram('NOUN')
    ADJF = gram('ADJF')
    ANIM=gram('anim')
    GENT=gram('gent')
    SGTM=gram('Sgtm')
    CONJ=gram('CONJ')
    PATR=gram('Patr')
    NAME = gram('Name')
    PREP=gram('PREP')


    STATE=or_(
        eq('моторин'),
        eq('юрок'),
        eq('вакула'),
        eq('эйхвальд'),
        eq('иммуно'),
        eq('из'),
        eq('славы'),
        eq('хайбулаев'),
        eq('михална'),
        eq('валиде'),
        eq('шиян'),
        eq('сим'),
        eq('мазитов'),
        eq('хамидов')
    )

    NAME_CONST=rule(
        and_(
        NAME,
        ANIM,
        not_(
            SGTM
        ),
            not_(STATE)
        )
    )

    COMPLICATED=rule(
        NAME_CONST.repeatable()
    )

    FINAL = or_(COMPLICATED)
    return FINAL

def get_second_rules():
    RU = type('RU')
    INT = type('INT')
    NONE = type('NONE')
    NOUN= gram('NOUN')
    ADJF = gram('ADJF')
    ANIM=gram('anim')
    GENT=gram('gent')
    SGTM=gram('Sgtm')
    FEMN=gram('femn')
    CONJ=gram('CONJ')
    PATR=gram('Patr')
    NAME = gram('Name')
    PREP=gram('PREP')


    SURNAME_CONST=rule(
        and_(
        SGTM,
        ANIM,
        not_(NAME),
        not_ (PATR),
        not_(eq('по')),
        not_(eq('ленина')),
        not_(eq('ульянова'))
        )
    )

    SURNAME=or_(
        SURNAME_CONST,
        rule(eq('Иванов')),
        rule(eq('левченко')),
        rule(eq('эйхвальд')),
        rule(eq('зимина')),
        rule(eq('хитарьян')),
        rule(eq('моторин')),
        rule(eq('рукавишников')),
        rule(eq('деткино')),
        rule(eq('буланцев')),
        rule(eq('багров')),
        rule(eq('шерл')),
        rule(eq('белоцерковский')),
        rule(eq('степанов')),
        rule(eq('шляхов')),
        rule(eq('моисеев')),
        rule(eq('пузанков')),
        rule(eq('попиченко')),
        rule(eq('сергеев')),
        rule(eq('удовенко')),
        rule(eq('тютин')),
        rule(eq('удовенко'))
    )

    COMPLICATED=rule(
        SURNAME.repeatable()
    )


    FINAL = or_(COMPLICATED)
    return FINAL