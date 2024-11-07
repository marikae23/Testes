#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int randomizer() {
    return rand() % 50 + 1;
}

void jogar(int *jogadas) {
    int numero = randomizer();
    int tentativas = 0;
    int chute = 0;
    int *historico = (int *)malloc(sizeof(int) * 50); 

    if (historico == NULL) {
        printf("Erro ao alocar memória para o histórico de tentativas.\n");
        return;
    }

    printf("Um número entre 1 e 50 foi escolhido. Vamos jogar!\n");
    
    while (1) {
        printf("Digite um número entre 1 e 50: ");
        scanf("%d", &chute);

        if (chute < 1 || chute > 50) {
            printf("Você digitou um número fora do intervalo (1-50). Tente novamente.\n");
            continue;
        }

        historico[tentativas] = chute; 
        tentativas++;
        
        if (chute > numero) {
            printf("Tente um número menor.\n");
        } else if (chute < numero) {
            printf("Tente um número maior.\n");
        } else {
            (*jogadas)++;
            printf("Você acertou! O número era %d.\n", numero);
            printf("Você usou %d tentativa(s) e jogou %d vez(es).\n", tentativas, *jogadas);
            printf("Histórico de tentativas: ");
            for (int i = 0; i < tentativas; i++) {
                printf("%d ", historico[i]);
            }
            printf("\n");
            break;
        }
    }

    free(historico);
}

int main() {
    srand(time(0));
    printf("Bem-vindo ao jogo de adivinhação!\n");
    
    char jogar_novamente;
    int jogadas = 0;

    do {
        jogar(&jogadas);
        printf("Deseja jogar novamente? (s/n): ");
        scanf(" %c", &jogar_novamente);
    } while (jogar_novamente == 's' || jogar_novamente == 'S');

    printf("Obrigado por jogar! Até a próxima.\n");
    return 0;
}
