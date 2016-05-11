# -*- coding: utf-8 -*-

import stack_chain


def expression(expressionStrings):  # 输入表达式字符串,如:'1 + 1 * 2'以空格空开
    allexpress = ['+', '-', '*', '/', '(', ')']
    orderEX = {  # 构建运算符优先级
        '(': [1,0],  # 第一位为优先级,第二位为标签
        ')': [1],
        '+': [3],
        '-': [3],
        '*': [2],
        '/': [2],
    }
    output = []  # 建立存放输出的列表
    p_expression = stack_chain.stackChain()  # 建立存放表达式的堆栈
    normalExpression = expressionStrings.split()
    for element in normalExpression:
        if not(element in allexpress):
            output.append(element)
        else:
            while not stack_chain.isEmpty(p_expression):  # 如果堆栈不为空,则开始判断
                topElement = stack_chain.pop(p_expression)  # 弹出栈顶元素并赋值给topElement
                if orderEX[topElement][0] <= orderEX[element][0]:  # 栈顶优先级低,则输出栈顶元素
                    if topElement == '(' and orderEX['('][1] == 0:  # 未弹出'(',将'('不断输入
                        stack_chain.push(p_expression, topElement)
                        stack_chain.push(p_expression, element)
                        break
                    elif topElement == ')':  # 遇到 ')'则改变'('的标签
                            orderEX['('][1] = 1
                    elif topElement == '(':
                            orderEX['('][1] = 0  # 当'('被pop出来后,初始化'('的标签
                    else:
                        output.append(topElement)
                else:  # 如果新扫到的运算符优先级低,则插入堆栈,并跳出循环
                        stack_chain.push(p_expression, topElement)  # 将栈顶元素重新插入
                        stack_chain.push(p_expression, element)  # 将新运算符也插入
                        break
            if stack_chain.isEmpty(p_expression):  # 如果堆栈为空,则说明元素没有push进去
                stack_chain.push(p_expression, element)
    while not(stack_chain.isEmpty(p_expression)):
        topElement = stack_chain.pop(p_expression)
        if not topElement in ['(', ')']:
            output.append(topElement)

    return output


#print(expression('2 * ( 9 + 6 / 3 - 5 ) + 4 * 2 * ( 2 + 1 )'))
