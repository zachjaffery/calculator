def drinkcalc(people,drinks_per):
  total_drinks = people*drinks_per
  total_mls = total_drinks*45
  total_fifths = -(-total_mls//750)
  total_handles = -(-total_mls//1750)
  return(total_fifths,total_handles)
