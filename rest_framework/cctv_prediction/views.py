from rest_framework.cctv_prediction.services import Service


class Crime_API(object):

    @staticmethod
    def main():

        crimeService = Service()

        while 1:
            m = input('0: Exit \n'
                      '1: 서울 cctv DF \n'
                      '2: 서울 범죄 DF \n'
                      '3: 경찰서 위치 DF \n'
                      '4: us_실업률 \n'
                      '5: pop in seoul \n')

            if m == '0':
                break

            elif m == '1':

                crimeService.csv({'context': './data/', 'fname': 'cctv_in_seoul'})

            elif m == '2':

                crimeService.csv({'context': './data/', 'fname': 'crime_in_seoul'})

            elif m == '3':

                crimeService.csv({'context': './data/', 'fname': 'police_position'})

            elif m == '4':

                crimeService.csv({'context': './data/', 'fname': 'us_unemployment'})

            elif m == '5':

                crimeService.xls({'context': './data/', 'fname': 'pop_in_seoul'})

            else:

                continue

Crime_API.main()