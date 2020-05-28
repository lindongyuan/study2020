#making_print_models调用
def print_modles(unprinted_designs,completed_models):
    '''模拟打印每个设计，直至所有列表内元素完成
    并将其移至completed_models中'''
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        #显示已打印信息
        #并添加至completed_models列表
        print("\nPrinting model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

