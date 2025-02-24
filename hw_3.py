import data
import build_data
import county_demographics

# Part 1:
# population_total(): returns the sum of the 2014 population attributes for all inputted
# county demographics objects within the list.
# input: list[data.CountyDemographics]
# output: int

def population_total(counties:list[data.CountyDemographics]) -> int:
    total = 0
    for county in counties:
        total += county.population['2014 Population']
    return total

#Part 2:
# filer_by_state(): returns a list of county objects that is filtered to only include
# counties which have the inputted state string as an attribute
# input: list[data.CountyDemographics], str
# output: list[CountyDemographics]

def filter_by_state(counties:list[data.CountyDemographics], state:str) -> list[data.CountyDemographics]:
    new_list = []
    try:
        for county in counties:
            if county.state == state:
                new_list.append(county)
    except KeyError:
        return []
    return new_list

#Part 3:

# population_by_education(): Returns the sum of the 2014 populations of every county object within the inputted list
# for the inputted education demographic
# input: list[data.CountyDemographics], str
# output: float

def population_by_education(counties:list[data.CountyDemographics], ed:str) -> float:
    total = 0
    try:
        for county in counties:
            ed_pop = county.population['2014 Population'] * (county.education[ed] * 0.01)
            total += ed_pop
    except KeyError:
        return 0
    return total


# population_by_ethnicity(): returns the sum of the 2014 populations across all counties within the inputted list
# within the inputted ethnicity
# input: list[data.CountyDemographics], str
# output: float
def population_by_ethnicity(counties:list[data.CountyDemographics], eth:str) -> float:
    total = 0
    try:
        for county in counties:
            eth_pop = county.population['2014 Population'] * (county.ethnicities[eth] * 0.01)
            total += eth_pop
    except KeyError:
        return 0
    return total


# population_below_poverty_level(): returns the total 2014 population across the inputted counties
# which are under the "below poverty level" demographic.
# input: list[data.CountyDemographics]
# output: float
def population_below_poverty_level(counties:list[data.CountyDemographics]) -> float:
    total = 0
    for county in counties:
        below_pop = county.population['2014 Population'] * (county.income['Persons Below Poverty Level'] * 0.01)
        total += below_pop
    return total


# percent_by_education(): returns the percentage of the 2014 population within an inputted education demographic
# across all county objects from the inputted list.
# input: list[data.CountyDemographics], str
# output: float

def percent_by_education(counties:list[data.CountyDemographics], ed:str) -> float:
    total = population_total(counties)
    sub_total = population_by_education(counties, ed)
    return sub_total / total


# percent_by_ethnicity(): returns the percent of the 2014 population within an inputted ethnicity demographic
# across all county objects from the inputted list.
# input: list[data.CountyDemographics], str
# output: float

def percent_by_ethnicity(counties:list[data.CountyDemographics], eth:str) -> float:
    total = population_total(counties)
    sub_total = population_by_ethnicity(counties, eth)
    return sub_total / total


# percent_below_poverty_level(): returns the percentage of the 2014 population within the
# "below poverty level" demographic across all county objects from the inputted list.
# input: list[data.County.Demographics]
# output: float

def percent_below_poverty_level(counties:list[data.CountyDemographics]) -> float:
    total = population_total(counties)
    sub_total = population_below_poverty_level(counties)
    return sub_total / total




