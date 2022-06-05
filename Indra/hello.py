def describe_pet(animal_type, pet_name):
  """Display information about a pet."""
  print("\nI have a " + animal_type + ".")
  print("My " + animal_type + "'s name is " + pet_name.title() + ".")
  print(f"I love my {animal_type}. His name is {pet_name.title()}")


describe_pet('Dog', 'xyz')

describe_pet(pet_name='harry', animal_type='hamster' )
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')