"""Reinicia as migrações

Revision ID: b9730c09f47c
Revises: 
Create Date: 2024-08-13 20:43:44.288940

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9730c09f47c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
       # Converte a coluna created_at para TIMESTAMP WITHOUT TIME ZONE usando a cláusula USING
       op.execute('ALTER TABLE elections_data ALTER COLUMN created_at TYPE TIMESTAMP WITHOUT TIME ZONE USING created_at::timestamp without time zone')

       # ### commands auto generated by Alembic - please adjust! ###
       with op.batch_alter_table('elections_data', schema=None) as batch_op:
              batch_op.alter_column('created_at',
                     existing_type=sa.VARCHAR(),
                     type_=sa.DateTime(),
                     existing_nullable=True,
                     existing_server_default=sa.text('CURRENT_TIMESTAMP'))
              batch_op.alter_column('updated_at',
                     existing_type=sa.VARCHAR(),
                     type_=sa.DateTime(),
                     existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
       # Reverte a coluna created_at para VARCHAR
       op.execute('ALTER TABLE elections_data ALTER COLUMN created_at TYPE VARCHAR')
       # ### commands auto generated by Alembic - please adjust! ###
       with op.batch_alter_table('elections_data', schema=None) as batch_op:
              batch_op.alter_column('updated_at',
                     existing_type=sa.DateTime(),
                     type_=sa.VARCHAR(),
                     existing_nullable=True)
              batch_op.alter_column('created_at',
                     existing_type=sa.DateTime(),
                     type_=sa.VARCHAR(),
                     existing_nullable=True,
                     existing_server_default=sa.text('CURRENT_TIMESTAMP'))

    # ### end Alembic commands ###
