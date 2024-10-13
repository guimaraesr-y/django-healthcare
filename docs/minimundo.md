## Minimundo

No sistema em desenvolvimento, há duas categorias principais de usuários: **gestores** e **colaboradores**. O sistema tem como principal objetivo auxiliar na gestão e acompanhamento de tarefas relacionadas aos **pacientes**, de modo que os gestores possam administrar o andamento das atividades e os colaboradores possam visualizar e finalizar as tarefas atribuídas a eles.

- O **gestor** é o único usuário que possui acesso completo ao sistema, sendo responsável por cadastrar, atualizar e gerenciar os dados dos **pacientes**, bem como dos **colaboradores**. Ele também atribui tarefas relacionadas aos pacientes aos colaboradores e acompanha a conclusão dessas atividades. 
- Os **colaboradores**, por sua vez, têm acesso apenas à visualização dos pacientes aos quais estão designados e das respectivas tarefas. Eles podem marcar as tarefas como concluídas após realizá-las, informando o gestor sobre o andamento do atendimento.

Cada **paciente** possui informações como nome, idade, gênero, e-mail, telefone, e pelo menos um **endereço** cadastrado, que é utilizado para saber onde as atividades devem ser realizadas, quando aplicável. Um paciente pode ter várias tarefas associadas a ele, as quais são atribuídas pelo gestor aos colaboradores.

As **tarefas** são descritas pelo gestor e estão sempre relacionadas a um paciente. Após a atribuição, qualquer colaborador pode realizá-la, contanto que esteja relacionado ao paciente. Quando o colaborador finaliza a tarefa, ele marca a atividade como concluída no sistema. 

O **endereço do paciente** é gerido pelo gestor e pode ser atualizado conforme necessário. Um paciente pode ter mais de um endereço registrado ao longo do tempo, sendo importante manter o endereço atual para facilitar o acompanhamento e a execução das tarefas pelos colaboradores.

As principais entidades do sistema são:
- **Paciente**: cadastrado pelo gestor, possui informações pessoais e um endereço.
- **Colaborador**: gerenciado pelo gestor, é responsável por visualizar e concluir as tarefas atribuídas a ele.
- **Tarefa**: relacionada a um paciente, atribuída a um colaborador pelo gestor, e pode ser marcada como concluída pelo colaborador.
- **Endereço do Paciente**: informações sobre o local de contato ou atendimento do paciente, gerenciado pelo gestor.

O sistema tem como foco principal garantir que o gestor tenha o controle sobre a gestão dos pacientes e o andamento das tarefas realizadas pelos colaboradores, enquanto os colaboradores apenas visualizam as informações e executam as tarefas.