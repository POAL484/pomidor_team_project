


class People():
    def __init__(self, age, name) -> None:
        self.age, self.name = age, name

    
    def __str__(self) -> str:
        return f'{self.age}, {self.name}'

    
    class Job():
        def __init__(self, job, z) -> None:
            self.job, self.z = job, z

        def get_data(self):
            return {'job': self.job,
                    'zarplata': self.z}
        
        def __str__(self) -> str:
            return f'{self.job}, {self.z}'
        


if __name__ == '__main__':
    mark = People(18, 'Mark')
    print(mark)
    job = mark.Job('worker', 100000)
    print(job)
    print(job.get_data())