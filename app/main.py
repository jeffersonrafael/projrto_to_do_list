import flet as ft

def main(page: ft.Page):
    # Título da página
    page.title = "App To-Do List"
    page.scroll = "adaptive"
    page.window_width = 360  # Largura padrão para 9:16
    page.window_height = 640  # Altura padrão para 9:16
    
    # Lista de categorias
    categories = {}

    # Função para adicionar uma nova categoria
    def add_category(e):
        category_name = category_name_input.value
        if category_name and category_name not in categories:
            categories[category_name] = []
            update_ui()
        category_name_input.value = ""
        page.update()

    # Função para adicionar uma nova tarefa em uma categoria
    def add_task(category):
        def add(e):
            task_name = task_name_input[category].current.value
            if task_name:
                categories[category].append({"name": task_name, "done": False})
                update_ui()
            task_name_input[category].current.value = ""
            page.update()
        return add

    # Função para marcar/desmarcar uma tarefa como concluída
    def toggle_task(category, task_index):
        def toggle(e):
            categories[category][task_index]["done"] = not categories[category][task_index]["done"]
            update_ui()
        return toggle

    # Função para atualizar a interface do usuário
    def update_ui():
        # Limpar a lista de categorias exibidas
        task_view.controls.clear()
        
        # Exibir cada categoria e suas tarefas
        for category, tasks in categories.items():
            category_tasks = [
                ft.Checkbox(
                    label=task["name"],
                    value=task["done"],
                    on_change=toggle_task(category, i)
                )
                for i, task in enumerate(tasks)
            ]
            task_view.controls.append(
                ft.Column([
                    ft.Text(category, style="headlineMedium"),
                    *category_tasks,
                    ft.TextField(ref=task_name_input.setdefault(category, ft.Ref()), hint_text="Nova Tarefa"),
                    ft.ElevatedButton("Adicionar Tarefa", on_click=add_task(category)),
                ], spacing=10)
            )

        page.update()

    # Componentes de entrada
    category_name_input = ft.TextField(hint_text="Nova Categoria")
    task_name_input = {}

    # Botão para adicionar categoria
    add_category_button = ft.ElevatedButton("Adicionar Categoria", on_click=add_category)

    # View para as tarefas
    task_view = ft.Column(spacing=20)

    # Layout principal
    page.add(
        ft.Column([
            ft.Row([category_name_input, add_category_button], alignment="start"),
            task_view
        ], spacing=20)
    )

# Executar o app
if __name__ == "__main__":
    # Código principal do programa
    ft.app(target=main)
