# sets a variable that calls input
# always use %s for formatting since %r will give the "representation" the raw version
formatter = "%r %r %r %r"

# call the variable with various input
print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
# this merely displays the variables parameters four times
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could typ. up right.",
	"But it didn't sing.",
	"So I said goodnight."
)