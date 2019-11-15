# Number Guessing Game
# Author : Gurpreet Sachdeva
# Email  : gurpreet.sachdevagss@yahoo.in
puts "Welcome to Number Guessing Game"
puts "You have to guess a number b/w 1-100 in max of 10 tries"
puts "Please tell us your name"
name=gets.chomp
puts "#{name}, Let's see if you can guess it right"
guessed_it=false
target=1+rand(100)
number_of_guesses=0
remaining_guesses=10
while number_of_guesses<10 and guessed_it==false
	puts "You have these many guesses remaining #{remaining_guesses}"
	puts "Enter the guess number"
	number=gets.to_i
	if number>target
		puts "Guess is higher than the computer target no"
	elsif number<target
		puts "Guess is lower than the computer target no"
	else number==target
		puts "You got it right mate"
		puts "Exiting game"
		guessed_it=true
	end
	number_of_guesses+=1
	remaining_guesses-=1
end
if not guessed_it
	puts "The target number is #{target}.Your 10 tries are exhausted"
end

