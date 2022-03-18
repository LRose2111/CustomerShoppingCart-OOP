class Product():

        def __init__(self):
            self.product_name = ''
            self.product_price = ''
            self.product_category = ''

        def name_of_product(self):
            product_name = self.product_name
            self.product_name = input(f'What is the name of the product? ')
            print(f'The product your buying is {self.product_name}.')

        def product_cost(self):
            cost = self.product_price
            self.product_price = input(f'How much is {self.product_name}?  ')
            print(f'{self.product_name} costs {self.product_price}.')

        def product_cate(self):
            category = self.product_category
            self.product_category = input(f'What category is {self.product_name} in? ')
            print(f'{self.product_name} is in the {self.product_category}.')
