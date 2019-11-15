class UserProfile
	def name
		@name
	end
	def name=(value)
		@name=value
	end
	def age
		@age
	end
	def age=(value)
		@age=value
	end
	def report_age
		puts "#{@name} is #{@age} years old"
	end
end
user=UserProfile.new
user.name="Saket"
user.age=42
user.report_age
