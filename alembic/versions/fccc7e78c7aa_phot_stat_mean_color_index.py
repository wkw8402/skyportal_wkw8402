"""phot stat mean color index

Revision ID: fccc7e78c7aa
Revises: 556169569def
Create Date: 2022-08-01 14:40:10.871788

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = 'fccc7e78c7aa'
down_revision = 'ef7f7859dbba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_photstats_mean_color'), table_name='photstats')

    op.create_index(
        op.f('ix_photstats_mean_color_gin'),
        'photstats',
        ['mean_color'],
        unique=False,
        postgresql_using="gin",
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_photstats_mean_color_gin'), table_name='photstats')
    op.create_index(
        op.f('ix_photstats_mean_color'), 'photstats', ['mean_color'], unique=False
    )
    # ### end Alembic commands ###
