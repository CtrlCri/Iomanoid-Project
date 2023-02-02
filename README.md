<h1 align="center" id="title">Iomanoid, Multi-Platform NFT Directory (Multi-Marketplace)</h1>

<p align="center"><img src="iomanoide.png" alt="project-image"></p>

<p id="description">Iomanoid's purpose is to be the most trusted NFT directory in the world.. We want to increase the visibility of Cryptoart or Digital Art, helping emerging and established artists with tools that allow them, from becoming visible to being able to create their own Web3 community. On the other hand, we want to help collectors to, for example, discover new talents and connect directly with them. But that's not all, we are also going to implement functionalities to Iomanoid that allow its users to learn about the technology behind NFTs and the Crypto ecosystem, Blockchain.</p>

## Features

Here're some of the project's best features:

* Post your NFT Project
* Publish your Giveaway, Whitelist or Waiting list events
* Get your "Link in Bio".
* And, if you are a collector or investor
Don't miss out on any potential projects!

## The process 
### Built with

Technologies used in the project:

*   Python
*   FastAPI
*   SQL-Alchemy
*   MySQL

### Iomanoid structure

``` Swift
// User struct
class User(Base):
    __tablename__ = "users"
    
    user_id = Column(Integer(), primary_key=True, autoincrement=True)
    user_name = Column(String(45), nullable=False, unique=True)
    email = Column(String(45), nullable=False, unique=True)
    password = Column(String(300))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime)

    projects = relationship("Project", back_populates="owner")
    
    __table_args__= {
        'mysql_engine':'InnoDB'
    }

```

``` Swift
// Project struct
class Project(Base):
    __tablename__ = "projects"
    
    project_id = Column(Integer(), primary_key=True, autoincrement=True)
    project_name = Column(String(45), nullable=False, unique=True)
    description = Column(String(450), nullable=False)
    owner_id = Column(Integer(), ForeignKey("users.user_id"), nullable=True)

    blockchain = Column(Enum('Polygon', 'Ethereum', 'Solana', 'Otro'))
    marketplace = Column(Enum('OpenSea', 'Rarible', 'Otro', 'En proceso'))
    marketplace_url = Column(String(300), nullable=True)
    collection_size = Column(Integer(), nullable=False)
    release_date = Column(DateTime, nullable=True) 
    
    instagram = Column(String(70), nullable=True)
    twitter = Column(String(70), nullable=True)
    discord = Column(String(70), nullable=True)
    website = Column(String(70), nullable=True)
    source = Column(String(70), nullable=True)

    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, nullable=True) 
    
    owner = relationship("User", back_populates="projects")

    __table_args__= {
        'mysql_engine':'InnoDB'
    }

```

## License:

> This project is licensed under the MIT License

Although a code host like GitHub may allow you to view and fork the code, this does not imply that you are authorized to use, modify, or share the software for any purpose. Please, if you want to collaborate with the project, send me an email to aramayoreyes@gmail.com

## Author

Made with 💙 by Cristian
