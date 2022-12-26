#See "Option 3": https://github.com/LIAAD/yake/blob/master/README.md
import yake

#JobDescription.txt should be the description you're analyzing, straight copy-paste
with open('JobDescription.txt') as file:
    job_description = str(file.readlines())
file.close()

#Extract 30 keywords from the stringified job description
keyword_extractor = yake.KeywordExtractor(top=100)
keywords = keyword_extractor.extract_keywords(job_description)

for keyword in keywords:
    print(keyword)