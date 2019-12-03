
library(tidyverse)

input <- read_csv("input.csv",col_names="mass")

get_fuel <- function(mass){
  return(fuel <- floor(mass/3)-2)
}

# Preprocess
input <- input %>%
  mutate(fuel = get_fuel(mass))

# Part 1
fuel_upper_modules <- input %>%
  summarise(fuel_upper = sum(fuel))
print(paste0("Part 1: ",fuel_upper_modules))

# Part 2
fuel_upper_fuel <- 0
for (row in 1:nrow(input)) {
  mass <- input[row, "fuel"] %>% pull()
  # print(paste0("Step: ",mass))
  continue_loop <- TRUE
  while (continue_loop == TRUE) {
    fuel <- get_fuel(mass)
    # print(paste0("Step: ",fuel))
    if (fuel > 0) {
      fuel_upper_fuel <- fuel_upper_fuel + fuel
      mass <- fuel
    } else {
      continue_loop <- FALSE
    }
  }
}
print(paste0("Part 2: ",fuel_upper_modules+fuel_upper_fuel))
