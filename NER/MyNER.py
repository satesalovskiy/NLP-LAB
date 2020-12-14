import street_rules
import cities_rules
import apparts_rules
import persons_rules
import unittest

from yargy import Parser, rule, and_, not_, or_
from yargy.interpretation import fact
import unittest
from yargy.predicates import gram
from yargy.predicates import eq, type
from yargy.relations import gnc_relation
from yargy.pipelines import morph_pipeline
from random import seed, sample
from ipymarkup import show_ascii_markup
from ipymarkup import show_box_markup
from yargy.tokenizer import MorphTokenizer


list_of_streets_suffixs = ['улица','тракт','бульвар','проспект',
    'микрорайон','проезд','шоссе']

class PersonsResult():
    first = None 
    middle = None 
    last = None 
    
class MyNER:

    def parseAddressMatches(self, matches):
        dom = None
        corpus = None
        room = None
        first = True
        specials = ['/']
        if(len (matches) != 0):
            if(len (matches[0].tokens) != 0):
                i = 0
                while i < len(matches[0].tokens):
                    if matches[0].tokens[i].value.isdigit():
                        if matches[0].tokens[i].value == '12' and i+1 < len (matches[0].tokens) and matches[0].tokens[i+1].value == 'мне':
                            break
                        if matches[0].tokens[i].value == '30' and i+1 < len (matches[0].tokens) and matches[0].tokens[i+1].value == 'лет':
                            room = matches[1].tokens[len(matches[0].tokens)-1].value
                            dom = matches[1].tokens[len(matches[0].tokens)-2].value
                            break
                        if first == True:
                            dom = matches[0].tokens[i].value
                            if i+1 < len (matches[0].tokens) and matches[0].tokens[i+1].value in specials: 
                                if i+2 < len (matches[0].tokens) and matches[0].tokens[i+2].value.isdigit():
                                    dom = dom + matches[0].tokens[i+1].value + matches[0].tokens[i+2].value
                            if i+1 < len (matches[0].tokens) and len(matches[0].tokens[i+1].value) == 1 and matches[0].tokens[i+1].value.isdigit() == False and matches[0].tokens[i+1].value !='/':
                                if i+2 < len (matches[0].tokens) and matches[0].tokens[i+2].value != 'улица':
                                    dom = dom + matches[0].tokens[i+1].value
                                elif i+2 >= len (matches[0].tokens):
                                    dom = dom + matches[0].tokens[i+1].value
                            if i+1 < len (matches[0].tokens) and matches[0].tokens[i+1].value.isdigit():
                                room = "" + matches[0].tokens[i+1].value
                            first = False 
                    if matches[0].tokens[i].value == 'корпус':
                        corpus = "" + matches[0].tokens[i+1].value
                    if matches[0].tokens[i].value == 'квартира':
                        room = "" + matches[0].tokens[i+1].value   
                    i += 1
        return (dom, corpus, room)   

    def parseStreetMatches(self, matches):
        street_type = None 
        street_name = None
        space_counter = 0
        if(len (matches) != 0):
            if(len (matches[0].tokens) != 0):
                street_name = ""
                for token in matches[0].tokens:
                    if token.value in list_of_streets_suffixs:
                        street_type = token.value
                    else:
                        if token.value == 'значит':
                            continue
                        if space_counter == 0:
                            street_name = street_name + token.value
                            space_counter = space_counter + 1
                        else:
                            street_name = street_name + " " + token.value                    
        return (street_name, street_type)

    def parseCitiesMatches(self, matches):
        city_type = None
        city_name = None 
        if(len (matches) != 0):
            if(len (matches[0].tokens) != 0):
                city_name = ""
                for token in matches[0].tokens:
                    if token.value == 'город':
                        city_type = token.value
                    # print(token.value)
                    else: 
                        if(city_name != ""):
                            city_name = city_name + " "
                        city_name = city_name + token.value 
        return (city_name, city_type)
    
    def nerStreet(self, string):
        rules = street_rules.get_rules()
        self.parser = Parser(rules)
        streetsMatches = list(self.parser.findall(string))
        res = self.parseStreetMatches(streetsMatches)    
        return res

    def nerCities(self, string):
        rules = cities_rules.get_rules()
        finalCityParser = Parser(rules)
        finalCityMatches = list(finalCityParser.findall(string))
        result = self.parseCitiesMatches(finalCityMatches)
        return result

    def nerApparts(self, string):
        rules = apparts_rules.get_rules()
        finalAppartParser = Parser(rules)
        finalAppartMatches = list(finalAppartParser.findall(string))
        result = self.parseAddressMatches(finalAppartMatches)
        return result

    def totalNERaddress(self, string):
        result_apparts = self.nerApparts(string)
        result_cities = self.nerCities(string)
        result_streets = self.nerStreet(string)
        return (result_apparts,result_cities,result_streets)

    def totalNERPersons(self, string):   
        res = PersonsResult()     

        rules = persons_rules.get_mid_rules()
        middleParser = Parser(rules)
        middle = list(middleParser.findall(string))
        res.middle = self.parseNameMatches(middle)


        rules = persons_rules.get_first_rules() 
        firstParser = Parser(rules)
        first = list(firstParser.findall(string))
        res.first = self.parseNameMatches(first)

        rules = persons_rules.get_second_rules() 
        lastParser = Parser(rules)
        last = list(lastParser.findall(string))
        res.last = self.parseNameMatches(last)

        return res

    def parseNameMatches(self, matches):
        res = None
        if(len (matches) != 0):
            if(len (matches[0].tokens) != 0):
                res = matches[0].tokens[0].value
        return res