#!/usr/bin/env python3
 
import logging 
import os
# BOILERPLATE = Código repetido em varios scripts
# TODO: user função
# TODO: usar lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
# Instacia logging
log = logging.Logger("Logs.py", log_level)
# level
ch = logging.StreamHandler() # Console/terminal/stderr
ch.setLevel(log_level)
# Formatação
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s'
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
# destino
log.addHandler(ch)


"""
log.debug("Mensagem pro dev, qe, sysadmin")
log.info("Mensagem geral para usuários")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta uma unica execução")
log.critical("Erro geral ex: banco de dados sumiu ")
"""

print("-" *50)
try: 
    1 / 0 
except ZeroDivisionError as e:
    log.error("Deu erro, %s}", str(e))
