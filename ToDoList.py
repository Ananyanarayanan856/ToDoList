class Todolist:
    def __init__(self, filename="todo.txt"):
        self.filename = filename
        self.tasks = []
        self.load_from_file()

    def load_from_file(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    description, status = line.strip().split(',')
                    task = {
                        'description': description,
                        'status': status == 'True'
                    }
                    self.tasks.append(task)
                    print(f'saved version loaded from {self.filename}')
        except FileNotFoundError:
            print('\n No previously saved versions found. Starting an empty To Do list\n')
    def add_task(self, description):
        task = {
            'description':description,
            'status':False
        }
        self.tasks.append(task)
        self.save_to_file()
        print(f'task\'{description}\'added successfully to the To Do list \n')

    def save_to_file(self):
        with open(self.filename, 'w')as file:
            for task in self.tasks:
                line = f'{task['description']},{task['status']}\n'
                file.write(line)


    def display_tasks(self):
        print("\n~~:To Do List:~~")

        pending_tasks=[task for task in self.tasks if not task['status']]
        completed_tasks=[task for task in self.tasks if task['status']]

        if not pending_tasks and not completed_tasks:
            print('\n No tasks available currently !')
        else:
            print('\n Pending tasks:-')
            for i, task in enumerate(pending_tasks, 1):
                print(f'{i}. {task['description']}[TO-DO]')

            print('\n Completed Tasks:-')
            for i, task in enumerate(completed_tasks,1):
                print(f'{i}. {task['description']} [DONE]')
                print('_________________________________\n')

    def mark_as_done(self,task_index):
        pending_tasks=[task for task in self.tasks if not task['status']]

        if 1 <= task_index <=len(pending_tasks):
            task = pending_tasks[task_index-1]
            task['status']=True
            self.save_to_file()
            print(f'task {task['description']} marked as done')

        else:
            print('\n Invalid task index')

    def remove_task(self, task_type, task_index):
        if task_type == 1:
            pending_tasks = [task for task in self.tasks if not task['status']]
            if 1<= task_index <= len(pending_tasks):
                task = pending_tasks[task_index-1] 
                self.tasks.remove(task)
                print(f'\n task{task['description']} removed from list successfully ')
            else:
                print('\n invalid task index')
        elif task_type == 2:
            completed_tasks = [task for task in self.tasks if not task ['status']]
            if 1 <= task_index <= len(completed_tasks):
                task = completed_tasks[task_index-1] 
                self.tasks.remove(task)
                print(f'\ntask {task['description']} removed from the list successfully')
            else:
                print('\n Invalid task index')
        else:
            print('\n Invalid choice')
        self.save_to_file()
def main():
        todolist =Todolist()

        while True:
            print('\n 1.Display Tasks \n 2.Add New task \n 3.Remove a task \n 4.Mark task as done \n 5.Quit')
            choice = input(' Please Enter your choice (1/2/3/4/5):')

            if choice =='1':
                todolist.display_tasks()
            elif choice =='2':
                description = input('\n Please enter task description:')
                todolist.add_task(description)
            elif choice =='3':
                todolist.display_tasks()
                print('\n Do you wanna remove from \n1.Pending tasks \n2.Completed tasks')
                task_type = int(input('choose the type: '))
                task_index = int(input('Enter the task index to remove: '))
                todolist.remove_task(task_type, task_index)
            elif choice == '4':
                todolist.display_tasks()
                task_index = int(input('\n Enter the task index to mark it as done:'))
                todolist.mark_as_done(task_index)
            elif choice == '5':
                print('Exiting the program! ')
                break
            else:
                print('\n Please enter a valid choice!')

if __name__ == "__main__":
    main()