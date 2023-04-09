"""empty message

Revision ID: 35bbdedc08df
Revises: 863a997ecd5f
Create Date: 2023-04-09 21:36:32.146657

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35bbdedc08df'
down_revision = '863a997ecd5f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fav', schema=None) as batch_op:
        batch_op.alter_column('id_user',
               existing_type=sa.INTEGER(),
               nullable=False)

    with op.batch_alter_table('pilots', schema=None) as batch_op:
        batch_op.drop_column('current')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pilots', schema=None) as batch_op:
        batch_op.add_column(sa.Column('current', sa.BOOLEAN(), autoincrement=False, nullable=False))

    with op.batch_alter_table('fav', schema=None) as batch_op:
        batch_op.alter_column('id_user',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
