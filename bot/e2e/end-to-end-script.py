# ## end_to_end story 1
# * cumprimentar: oi
#     - utter_cumprimentar
# * importar_json: csv
#     - utter_importar_json_pandas
# * afirmar: aasdfasd
#     - utter_importar_json_pandas1
# * despedir: tchau
#     - utter_despedir

user_intent = [
    'cumprimentar',
    'importar_json',
    'transformar_dados_categoricos',
    'entender_metricas_de_classificacao',
    'entender_relatorio_classificacao',
    'entender_matriz_confusao',
    'entender_correlacao',
    'entender_decision_tree',
    'entender_explained_variance_score',
    'entender_feature_scaling',
    'entender_regressao_logistica',
    'oferecer_ajuda',
    'criar_histograma',
    'duvidas_de_como_implementar',
    'sobre_pyter',
    'importar_json_pandas'
    'afirmar',
    'kmeans_conceito',
    'entender_dados_faltantes',
    'entender_gaussian_naive_bayes',
    'entender_nearest_neighbors',
    'exemplo_funcao_r2_score',
    'entender_descentramento_estocástico_gradiente',
    'entender_maquina_de_vetores_de_suporte'

]

user_input = [
    'oi',
    'csv',
    'dados categoricos',
    'metricas de classificacao',
    'relatorio de classificacao',
    'entender matriz de confusão',
    'explicar correlacao',
    'decision tree',
    'entender explained score',
    'saber sobre feature scaling',
    'regressao logistica',
    'preciso de ajuda',
    'como criar um histograma',
    'como importar um arquivo csv',
    'quem eh voce',
    'como importar json',
    'sim',
    'o que e kmeans',
    'o que sao dados faltantes',
    'o que e gaussian naive bayes',
    'explique nearest neighbors',
    'como usar r2 score',
    'o que é descentramento estocástico gradiente',
    'o que eh maquina de vetores de suporte'
]

utter = [
    'utter_cumprimentar',
    'utter_importar_json_pandas',
    'utter_transformar_dados_categoricos',
    'utter_entender_metricas_de_classificacao',
    'utter_entender_relatorio_classificacao',
    'utter_entender_matriz_confusao',
    'utter_entender_correlacao',
    'utter_entender_gaussian_naive_bayes',
    'utter_entender_explained_variance_score',
    'utter_entender_feature_scaling',
    'utter_entender_regressao_logistica',
    'utter_ajuda',
    'utter_criar_histograma',
    'utter_tirar_duvidas_de_implementacao',
    'utter_sobre_pyter',
    'utter_importar_json_pandas',
    'utter_importar_json_pandas1',
    'utter_kmeans_conceitual',
    'utter_entender_dados_faltantes',
    'utter_entender_gaussian_naive_bayes',
    'utter_entender_nearest_neighbors',
    'utter_exemplo_funcao_r2_score',
    'utter_entender_descentramento_estocástico_gradiente',
    'utter_entender_maquina_de_vetores_de_suporte'
]

def create_stories(user_intent, user_input, utter):
    for intent, inp, utt in zip(user_intent, user_input, utter):
        yield "* {}: {}\n\t - {}".format(intent, inp, utt)


def write_file(stories):
    E2E_FILE = './e2e_stories.md'
    with open(E2E_FILE, "w") as f:
        stories = [story for story in stories]
        for story in stories:
            f.write("%s\n" % story)

stories = create_stories(user_intent, user_input, utter)
write_file(stories)
