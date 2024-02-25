
from cohere.responses.classify import Example

CLASSIFIER_EXAMPLES = [
    Example("Could you help me remember at what time my next math exam is?", "time_task"),
    Example("Do you remember where I left my keys?", "not_time_task"),
    Example("Will I have a class at 9am tomorrow?", "time_task"),
    Example("Do you remember how many classes I have tomorrow?", "time_task"),
    Example("I\'ve been having a good day", "not_time_task"),
    Example("Tomorrow is gonna be a good day!", "not_time_task"),
    Example("I got 100 on my exam yesterday!", "not_time_task"),
    Example("What events do I have planned for Saturday?", "time_task"),
    Example("Could you remind me to check the oven in 1 hour?", "time_task"),
    Example("Please remind me of my test on Saturday", "time_task"),
    Example("The party on Saturday was crazy!", "not_time_task"),
    Example("Remember I have math classes every Saturday", "time_task"),
    Example("Do you remember what days I have philosophy classes?", "time_task"),
    Example("I saw a very cute dog today!", "not_time_task"),
    Example("Did you know that humans sleep for 8 hours on average!", "not_time_task"),
    Example("How much time should I spend on my workout today?", "not_time_task"),
    Example("When is my next workout?", "time_task"),
    Example("I\'m worried about my upcoming test", "not_time_task"),
    Example("I have a gym session tomorrow", "not_time_task"),
    Example("Remember I have a gym session next week", "time_task"),
    Example("Do you remember what happened to my watch?", "not_time_task"),
    Example("Do you know what happened yesterday?", "time_task"),
    Example("What would happen to a potato if I left it on the freezer for 24 hours?", "not_time_task"),
    Example("Did I leave my food in the oven for more than 2 hours?", "time_task"),
    Example("Last Thursday I went to the park", "not_time_task"),
    Example("Do I train every week?", "time_task"),
    Example("Do teachers work every Saturday?", "not_time_task"),
    Example("Does Kevin have class in 2 hours?", "not_time_task"),
    Example("Do I have class in 10 hours?", "time_task")
]