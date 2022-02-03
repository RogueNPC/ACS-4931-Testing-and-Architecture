# by Kami Bigdely
# Split temporary variable

patty_gr = 70 # [gr]
pickle_gr = 20 # [gr]
tomatoes_gr = 25 # [gr]
lettuce_gr = 15 # [gr]
buns_gr = 95 # [gr]
kimchi_gr = 30 # [gr]
mayo_gr = 5 # [gr]
golden_fried_onion_gr = 20 # [gr]

ny_burger_weight = (2 * patty_gr + 
                    4 * pickle_gr + 
                    3 * tomatoes_gr + 
                    2 * lettuce_gr + 
                    2 * buns_gr)
print("NY Burger Weight", ny_burger_weight)

sk_burger_weight = (2 * patty_gr + 
                    4 * pickle_gr + 
                    3 * tomatoes_gr + 
                        kimchi_gr + 
                        mayo_gr + 
                        golden_fried_onion_gr + 
                    2 * buns_gr)
print("Seoul Kimchi Burger Weight", sk_burger_weight)

