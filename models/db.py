db = DAL('sqlite://storage.sqlite')

from gluon.tools import Auth

auth = Auth(db)
auth.settings.extra_fields['auth_user'] = [ Field('dp', 'upload', label='Your Profile Picture', requires=IS_NOT_EMPTY(error_message='cannot be empty')), Field('moderator', 'boolean', default = False, writable = False, readable = False)]
auth.settings.login_next = URL('homepage')
auth.define_tables(username=True)

db.define_table('images',
                Field('image', 'upload'),
                Field('title', 'string', unique = True),
                Field('author', 'integer'),
                Field('upload_time', 'datetime'),
                Field('caption', 'string'),
                Field('num_like', 'integer', default = 0, readable = False, writable = False),
                Field('num_wow', 'integer', default = 0, readable = False, writable = False),
                Field('num_angry', 'integer', default = 0, readable = False, writable = False),
                Field('num_sad', 'integer', default = 0, readable = False, writable = False),
                Field('num_haha', 'integer', default = 0, readable = False, writable = False)
                )
db.images.id.readable = False
db.images.upload_time.readable = db.images.upload_time.writable = False
db.images.author.readable = db.images.author.writable = False
db.images.title.requires = IS_NOT_EMPTY(error_message = 'cannot be empty!')
db.images.title.requires = IS_NOT_IN_DB(db, 'images.title', error_message = 'cannot be empty!')

db.define_table('comments',
                Field('comment', 'string', requires = IS_NOT_EMPTY(error_message = 'cannot be empty!')),
                Field('image_id', 'integer'),
                Field('userid', 'integer'),
                Field('upload_time', 'datetime')
                )

db.define_table('likes',
                Field('typeof', 'integer', readable = False, writable = False),
                Field('imageid', 'integer', readable = False, writable = False),
                Field('userid', 'integer', readable = False, writable = False)
                )

db.define_table('tags',
                Field('tagname', 'string'),
                Field('imageid', 'integer', readable = False, writable = False),
                Field('userid', 'integer', readable = False, writable = False),
                Field('verified', 'boolean', readable = False, writable = False)
                )

db.define_table('offense',
                Field('imageid', 'integer', unique = True, readable = False, writable = False),
                Field('numoff', 'integer', default = 1, readable = False, writable = False)
                )
