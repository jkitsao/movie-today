"""Add review title column to Review table

Revision ID: e58754fd26b9
Revises: a866b917de56
Create Date: 2019-10-20 14:42:40.418745

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e58754fd26b9'
down_revision = 'a866b917de56'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('review_title', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reviews', 'review_title')
    # ### end Alembic commands ###
