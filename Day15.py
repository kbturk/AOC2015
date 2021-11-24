import sys, argparse
from typing import List, Dict, NamedTuple, Tuple, Iterable
from pprint import pprint

class Ingredient(NamedTuple):
    name: str
    cap: int
    dur: int
    flav: int
    text: int
    cal: int

Recipe = List[Tuple[int, Ingredient]]

def arg_parser():
    parser = argparse.ArgumentParser(description="input file")
    parser.add_argument('input_file', help = 'please provide input file.', type = argparse.FileType('r'))
    return parser

def comb_tot(cookie: Recipe) -> Tuple[int, int]:
    cap_tot = 0
    dur_tot = 0
    flav_tot = 0
    text_tot = 0
    cal_tot = 0

    for k in cookie:
        cap_tot += k[1].cap*k[0]
        dur_tot += k[1].dur*k[0]
        flav_tot += k[1].flav*k[0]
        text_tot += k[1].text*k[0]
        cal_tot += k[1].cal*k[0]
    return max(cap_tot,0) * max(dur_tot,0) * max(flav_tot,0) * max(text_tot,0), cal_tot

def all_recipes(tsp: int, ingredients: List[Ingredient]) -> Iterable[Recipe]:
    match ingredients:
        case []: return
        case[ing]: yield[(tsp, ing)]
        case[first, *rest]:
            for k in range(tsp+1):
                for rest_recipe in all_recipes(tsp - k, rest):
                    yield [(k, first)] + rest_recipe

def winning_combination(recipies: List[Recipe]) -> Dict[str,int]:
    cookie_score: int = 0
    best_cookie_score = 0
    for recipe in recipies:
        cookie_score, cal_tot = comb_tot(recipe)
        if cookie_score > best_cookie_score and cal_tot == 500:
            best_cookie_score = cookie_score
            best_recipe = recipe
    print(best_recipe)
    return best_cookie_score

def main(argv: List[str]) -> int:
    input = arg_parser().parse_args(argv[1:]).input_file
    ingredients: List[Ingredient] = []
    for line in input:
        name, _, a, _, b, _, c, _, d, _, e = line.rstrip('\n').split()
        ingredients.append(Ingredient(name, int(a.rstrip(',')), int(b.rstrip(',')), int(c.rstrip(',')), int(d.rstrip(',')), int(e.rstrip(','))))
    recipes = all_recipes(100, ingredients)
    print(winning_combination(recipes))
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))