#MODULOS
import bdb
import distutils
import glob
import json
import logging
import os
import re
import shutil
import sys
import tempfile
import threading
import time
import traceback
import warnings

#COLORES
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"  # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"   # White
R = "\033[31m"    # Red
C = "\033[36;1m"  # Cyan
M = "\033[35;1m"  # Morado

#FUNCIONES
def corrida(s):
	for c in + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(3. / 250)

def valletta(s):
	for c in + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(2. / 120)
		
def saludo(s):
	for c in + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(3. / 100)

def medio(s):
	for c in + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(8. / 200)

def lento(s):
	for c in + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(10. / 200)
		

		#------------->BIENVENIDA
os.system("clear")
os.system("sleep 1")
print (M+"Abriendo Programa final...")

print (" ")

os.system("sleep 1")

print (R+"V.")

print (" ")

print (C+"T.")

print (" ")

print (G+"A.")

print (" ")

os.system("sleep 1")
#------------------->INTERFAZ DE BIENVENIDA
print (CC+"      V                V")
os.system("sleep 1")
print (RR+"       V              V ")
os.system("sleep 1")
print (YY+"        V            V  ")
os.system("sleep 1")
print (GG+"         V          V   ")
os.system("sleep 1")
print (CC+"          V        V    ")
os.system("sleep 1")
print (RR+"           V      V     ")
os.system("sleep 1")
print (YY+"            V    V      ")
os.system("sleep 1")
print (GG+"             V  V       ")
os.system("sleep 1")
print (CC+"              VV        ")
print (" ")
print (" ")
print (" ")

os.system("sleep 1")
print (C+"Hola! muy buenas tardes, mi nombre es V. soy el proyecto final de itachi, un gusto conocerte ")

print (" ")
print (" ")

os.system("sleep 2")

print (R+" 1) decir nombre ")
print (R+" 2) no decir nombre ")

print (" ")

eleccion = input("que elijes? ")

if eleccion == "1":
	def si():
		os.system("sleep 1")
		print (Y+"	User	  ")
		print (" ")
		os.system("sleep 1")
		print (RR+"	1)Profesor")
		print (CC+"	2)Itachi  ")
		print (YY+"	3)Ari	  ")
		print (GL+"	4)Jhon	  ")
		print (R+"	5)Mama Coco")
		print (C+"	6)Valeria ")
		print (" ")
		resposta = input(R+"	Usuario ")
		if resposta == "1":
			def Profesor():
				os.system("sleep 1")
				print (RR+"Un gusto tenerlo aqui, Profesor...")
			Profesor()
		elif resposta == "2":
			def Itachi():
				os.system("sleep 1")
				print (CC+"Un gusto tenerlo aqui, Owner...")
			Itachi()
		elif resposta == "3":
			def Ari():
				os.system("sleep 1")
				print (YY+"Pierdete soplagaitas (eso me lo enseno un colega)")
			Ari()
		elif resposta == "4":
			def Jhon():
				os.system("sleep 1")
				print (GL+"Saludos estudiante Jhon Doe...")
			Jhon()
		elif resposta == "5":
			def MamaCoco():
				os.system("sleep 1")
				print (R+"Saludos estudiante Coco Rivera...")
			MamaCoco()
		elif resposta == "6":
			def Valeria():
				os.system("sleep 1")
				print (C+"Saludos estudiante H Valeria...")
			Valeria()
		else:
			print (R+"El numero que has elejido no esta dentro de la lista...")		
	si()
	
elif eleccion == "2":
	def no():
		os.system("sleep 1")
		print (R+"ser anonimo es una base muy importante...")
	no()

else:
	print (R+"El numero que has elejido no esta dentro de la lista...")
	
#------------------->IMPORTANTE
print (" ")

os.system("sleep 2")

print (B+" coff coff, mejor sigamos... ")

print (" ")

os.system("sleep 1")
print (C+"quieres conocer las funciones de V?")

print (RR+" 1)Si")
print (WW+" 2)No")

print (" ")
respuesta = input(Y+" que deseas hacer? ")

if respuesta == "1":
	def profe():
		print (C+"Yo te las puedo mostrar...")
		os.system("sleep 1")
		print (R+" como ya sabras me llamo V. soy el trbajo final de itachi, yo me encargo de ejecutar diferentes tipos de funciones...")
		os.system("sleep 2")
		print (M+"poseo muchas funciones, desde un instalador de paquetes, un sistema de ataque SQL")
		os.system("sleep 2")
		print (CC+"tambien puedo proporcionar consejos basicos a los nuevos")
		os.system("sleep 1")
		print (YY+"entre otras cosas")
		os.system("sleep 1")
		print (R+"psd:	")
		print (GG+"soy un proyecto en fase beta")
		os.system("sleep 1")
		print (WW+"asi que mi creador se encargara de anadir nuevas funciones conforme el vaya aprendiendo...")
		os.system("sleep 1")
	profe()
	
elif respuesta == "2":
	def feo():
		os.system("sleep 1")
		print ("Sigamos...")
	feo()

#---------------->EMPEZANDO CON LAS FUNCIONES DE V.
os.system("sleep 1")
print (" ")

os.system("sleep 1")
print (YY+"     1) Consejos             ")
print (CC+"     2) instalador de paquetes")
print (WW+"     3) SQL (directamente)           ")
print (" ")

respuesta2 = input(C+"que quieres hacer? ")

if respuesta2 == "1":
	def Yon():
		os.system("sleep 1")
		print (R+"usted ah elijido la opcion de consejos, y yo puedo proporcionarlos...")
		print (" ")
		print (M+"	1> Manipulacion de Archivos")
		print (G+"	2> como utilizar los repositorios")
		print (" ")
		reply = input("que elijes: ")
		if reply == "1":
			def lol():
				os.system("sleep 1")
				print (C+"manipulacion de archivos")
				os.system("sleep 1")
				print (Y+"--__RENOMBRAR__--")
				print (RR+"mv + nombre del archivo + nuevo nombre")
				os.system("sleep 1")
				print ("--__MOVER__--")
				print (M+"mv + nombre del archio + nueva ruta del archivo")
				os.system("sleep 1")
				print (YY+"--__COPIAR__--")
				print (CC+"cp + nombre del archivo + nueva ruta del archivo")
				print (C+"Psd: ")
				print ("para mover carpetas se introduce el -r despues de el cp")
			lol()
		elif reply == "2":
			def lal():
				os.system("sleep 1")
				print (C+"los repositorios son carpetas con archivos dentro que cumplen con una funcion en especifico")
				os.system("sleep 1")
				print (R+"normalmente, se instalan los paquetes, se instala el repositorio y despues de eso, se entra con el comando cd")
				os.system("sleep 1")
				print (M+"al entrar con el comando cd, se aplica el comando ls para ver lo que hay dentro del repositorio")
				os.system("sleep 1")
				print (Y+"y se ejecuta con un comando en especifico, por ejemplo si el archivo esta escrito bajo python (.py)")
				os.system("sleep 1")
				print (C+"se ejecutara python + el nombre del archivo")
			lal()	
	Yon()	
	
elif respuesta2 == "2":
	def hitachi():
		os.system("sleep 1")
		print (CC+" que deseas instalar?")
		print (" ")
		os.system("sleep 1")
		print (BB+" 1) python")
		print (YY+" 2) nano")
		print (RR+" 3) cmatrix")
		print (" ")
		os.system("sleep 1")
		respuestas = input(W+"Que deseas hacer? ")
		if respuestas == "1":
			def nose():
				os.system("sleep 1")
				print (CC+"elejiste instalar el paquete python")
				os.system("sleep 1;pkg install python")
				print (RR+"instalando paquete python...")
			nose()
		elif respuestas == "2":
			def sise():
				os.system("sleep 1")
				print (C+"elejiste instalar el paquete nano")
				os.system("sleep 1;pkg install nano")
				print (R+"instalando paquete nano...")
			sise()
		elif respuestas == "3":
			def nosi():
				os.system("sleep 1")
				print (RR+"elejiste instalar el paquete cmatrix")
				os.system("sleep 1;pkg install cmatrix")
				print (CC+"instalando cmatrix...")
			nosi()
		else:
			 print ("intenta con otro numero...")
	hitachi()

elif respuesta2 == "3":
	def ala():
		print (" ")
		os.system("sleep 2")
		print ("Usted ah elejido el sql, para iniciarlo de manera correcta es necesario ejecutar el programa como si fuera el sql normalmente....")
		os.system("sleep 1")
		print ("Iniciando SQL")
		os.system("sleep 3")
	ala()
	
print (" ")
print (" ")
os.system("sleep 2")
print ("ara iniciarlo de manera correcta es necesario ejecutar el programa como si fuera el sql normalmente....")
os.system("sleep 1")
print ("Iniciando SQL")
os.system("sleep 3")

#!/usr/bin/env python

"""
Copyright (c) 2006-2021 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""


try:
    import sys

    sys.dont_write_bytecode = True

    try:
        __import__("lib.utils.versioncheck")  # this has to be the first non-standard import
    except ImportError:
        sys.exit("[!] wrong installation detected (missing modules). Visit 'https://github.com/sqlmapproject/sqlmap/#installation' for further details")

	

    warnings.filterwarnings(action="ignore", message="Python 2 is no longer supported")
    warnings.filterwarnings(action="ignore", message=".*was already imported", category=UserWarning)
    warnings.filterwarnings(action="ignore", message=".*using a very old release", category=UserWarning)
    warnings.filterwarnings(action="ignore", message=".*default buffer size will be used", category=RuntimeWarning)
    warnings.filterwarnings(action="ignore", category=DeprecationWarning)
    warnings.filterwarnings(action="ignore", category=UserWarning, module="psycopg2")

    from lib.core.data import logger
    from lib.core.common import banner
    from lib.core.common import checkIntegrity
    from lib.core.common import checkPipedInput
    from lib.core.common import createGithubIssue
    from lib.core.common import dataToStdout
    from lib.core.common import filterNone
    from lib.core.common import getDaysFromLastUpdate
    from lib.core.common import getFileItems
    from lib.core.common import getSafeExString
    from lib.core.common import maskSensitiveData
    from lib.core.common import openFile
    from lib.core.common import setPaths
    from lib.core.common import weAreFrozen
    from lib.core.convert import getUnicode
    from lib.core.data import cmdLineOptions
    from lib.core.data import conf
    from lib.core.data import kb
    from lib.core.common import MKSTEMP_PREFIX
    from lib.core.common import setColor
    from lib.core.common import unhandledExceptionMessage
    from lib.core.compat import xrange
    from lib.core.exception import SqlmapBaseException
    from lib.core.exception import SqlmapShellQuitException
    from lib.core.exception import SqlmapSilentQuitException
    from lib.core.exception import SqlmapUserQuitException
    from lib.core.option import init
    from lib.core.option import initOptions
    from lib.core.patch import dirtyPatches
    from lib.core.patch import resolveCrossReferences
    from lib.core.settings import GIT_PAGE
    from lib.core.settings import IS_WIN
    from lib.core.settings import LAST_UPDATE_NAGGING_DAYS
    from lib.core.settings import LEGAL_DISCLAIMER
    from lib.core.settings import THREAD_FINALIZATION_TIMEOUT
    from lib.core.settings import UNICODE_ENCODING
    from lib.core.settings import VERSION
    from lib.parse.cmdline import cmdLineParser
    from lib.utils.crawler import crawl
except KeyboardInterrupt:
    errMsg = "user aborted"

    if "logger" in globals():
        logger.critical(errMsg)
        raise SystemExit
    else:
        import time
        sys.exit("\r[%s] [CRITICAL] %s" % (time.strftime("%X"), errMsg))

def modulePath():
    """
    This will get us the program's directory, even if we are frozen
    using py2exe
    """

    try:
        _ = sys.executable if weAreFrozen() else __file__
    except NameError:
        _ = inspect.getsourcefile(modulePath)

    return getUnicode(os.path.dirname(os.path.realpath(_)), encoding=sys.getfilesystemencoding() or UNICODE_ENCODING)

def checkEnvironment():
    try:
        os.path.isdir(modulePath())
    except UnicodeEncodeError:
        errMsg = "your system does not properly handle non-ASCII paths. "
        errMsg += "Please move the sqlmap's directory to the other location"
        logger.critical(errMsg)
        raise SystemExit

    if distutils.version.LooseVersion(VERSION) < distutils.version.LooseVersion("1.0"):
        errMsg = "your runtime environment (e.g. PYTHONPATH) is "
        errMsg += "broken. Please make sure that you are not running "
        errMsg += "newer versions of sqlmap with runtime scripts for older "
        errMsg += "versions"
        logger.critical(errMsg)
        raise SystemExit

    # Patch for pip (import) environment
    if "sqlmap.sqlmap" in sys.modules:
        for _ in ("cmdLineOptions", "conf", "kb"):
            globals()[_] = getattr(sys.modules["lib.core.data"], _)

        for _ in ("SqlmapBaseException", "SqlmapShellQuitException", "SqlmapSilentQuitException", "SqlmapUserQuitException"):
            globals()[_] = getattr(sys.modules["lib.core.exception"], _)

def main():
    """
    Main function of sqlmap when running from command line.
    """

    try:
        dirtyPatches()
        resolveCrossReferences()
        checkEnvironment()
        setPaths(modulePath())
        banner()

        # Store original command line options for possible later restoration
        args = cmdLineParser()
        cmdLineOptions.update(args.__dict__ if hasattr(args, "__dict__") else args)
        initOptions(cmdLineOptions)

        if checkPipedInput():
            conf.batch = True

        if conf.get("api"):
            # heavy imports
            from lib.utils.api import StdDbOut
            from lib.utils.api import setRestAPILog

            # Overwrite system standard output and standard error to write
            # to an IPC database
            sys.stdout = StdDbOut(conf.taskid, messagetype="stdout")
            sys.stderr = StdDbOut(conf.taskid, messagetype="stderr")
            setRestAPILog()

        conf.showTime = True
        dataToStdout("[!] legal disclaimer: %s\n\n" % LEGAL_DISCLAIMER, forceOutput=True)
        dataToStdout("[*] starting @ %s\n\n" % time.strftime("%X /%Y-%m-%d/"), forceOutput=True)

        init()

        if not conf.updateAll:
            # Postponed imports (faster start)
            if conf.smokeTest:
                from lib.core.testing import smokeTest
                os._exitcode = 1 - (smokeTest() or 0)
            elif conf.vulnTest:
                from lib.core.testing import vulnTest
                os._exitcode = 1 - (vulnTest() or 0)
            elif conf.bedTest:
                from lib.core.testing import bedTest
                os._exitcode = 1 - (bedTest() or 0)
            elif conf.fuzzTest:
                from lib.core.testing import fuzzTest
                fuzzTest()
            else:
                from lib.controller.controller import start
                if conf.profile:
                    from lib.core.profiling import profile
                    globals()["start"] = start
                    profile()
                else:
                    try:
                        if conf.crawlDepth and conf.bulkFile:
                            targets = getFileItems(conf.bulkFile)

                            for i in xrange(len(targets)):
                                try:
                                    kb.targets.clear()
                                    target = targets[i]

                                    if not re.search(r"(?i)\Ahttp[s]*://", target):
                                        target = "http://%s" % target

                                    infoMsg = "starting crawler for target URL '%s' (%d/%d)" % (target, i + 1, len(targets))
                                    logger.info(infoMsg)

                                    crawl(target)
                                except Exception as ex:
                                    if not isinstance(ex, SqlmapUserQuitException):
                                        errMsg = "problem occurred while crawling '%s' ('%s')" % (target, getSafeExString(ex))
                                        logger.error(errMsg)
                                    else:
                                        raise
                                else:
                                    if kb.targets:
                                        start()
                        else:
                            start()
                    except Exception as ex:
                        os._exitcode = 1

                        if "can't start new thread" in getSafeExString(ex):
                            errMsg = "unable to start new threads. Please check OS (u)limits"
                            logger.critical(errMsg)
                            raise SystemExit
                        else:
                            raise

    except SqlmapUserQuitException:
        if not conf.batch:
            errMsg = "user quit"
            logger.error(errMsg)

    except (SqlmapSilentQuitException, bdb.BdbQuit):
        pass

    except SqlmapShellQuitException:
        cmdLineOptions.sqlmapShell = False

    except SqlmapBaseException as ex:
        errMsg = getSafeExString(ex)
        logger.critical(errMsg)

        os._exitcode = 1

        raise SystemExit

    except KeyboardInterrupt:
        print()

    except EOFError:
        print()

        errMsg = "exit"
        logger.error(errMsg)

    except SystemExit as ex:
        os._exitcode = ex.code or 0

    except:
        print()
        errMsg = unhandledExceptionMessage()
        excMsg = traceback.format_exc()
        valid = checkIntegrity()

        os._exitcode = 255

        if any(_ in excMsg for _ in ("MemoryError", "Cannot allocate memory")):
            errMsg = "memory exhaustion detected"
            logger.critical(errMsg)
            raise SystemExit

        elif any(_ in excMsg for _ in ("No space left", "Disk quota exceeded", "Disk full while accessing")):
            errMsg = "no space left on output device"
            logger.critical(errMsg)
            raise SystemExit

        elif any(_ in excMsg for _ in ("The paging file is too small",)):
            errMsg = "no space left for paging file"
            logger.critical(errMsg)
            raise SystemExit

        elif all(_ in excMsg for _ in ("Access is denied", "subprocess", "metasploit")):
            errMsg = "permission error occurred while running Metasploit"
            logger.critical(errMsg)
            raise SystemExit

        elif all(_ in excMsg for _ in ("Permission denied", "metasploit")):
            errMsg = "permission error occurred while using Metasploit"
            logger.critical(errMsg)
            raise SystemExit

        elif "Read-only file system" in excMsg:
            errMsg = "output device is mounted as read-only"
            logger.critical(errMsg)
            raise SystemExit

        elif "Insufficient system resources" in excMsg:
            errMsg = "resource exhaustion detected"
            logger.critical(errMsg)
            raise SystemExit

        elif "OperationalError: disk I/O error" in excMsg:
            errMsg = "I/O error on output device"
            logger.critical(errMsg)
            raise SystemExit

        elif "Violation of BIDI" in excMsg:
            errMsg = "invalid URL (violation of Bidi IDNA rule - RFC 5893)"
            logger.critical(errMsg)
            raise SystemExit

        elif "Invalid IPv6 URL" in excMsg:
            errMsg = "invalid URL ('%s')" % excMsg.strip().split('\n')[-1]
            logger.critical(errMsg)
            raise SystemExit

        elif "_mkstemp_inner" in excMsg:
            errMsg = "there has been a problem while accessing temporary files"
            logger.critical(errMsg)
            raise SystemExit

        elif any(_ in excMsg for _ in ("tempfile.mkdtemp", "tempfile.mkstemp", "tempfile.py")):
            errMsg = "unable to write to the temporary directory '%s'. " % tempfile.gettempdir()
            errMsg += "Please make sure that your disk is not full and "
            errMsg += "that you have sufficient write permissions to "
            errMsg += "create temporary files and/or directories"
            logger.critical(errMsg)
            raise SystemExit

        elif "Permission denied: '" in excMsg:
            match = re.search(r"Permission denied: '([^']*)", excMsg)
            errMsg = "permission error occurred while accessing file '%s'" % match.group(1)
            logger.critical(errMsg)
            raise SystemExit

        elif all(_ in excMsg for _ in ("twophase", "sqlalchemy")):
            errMsg = "please update the 'sqlalchemy' package (>= 1.1.11) "
            errMsg += "(Reference: 'https://qiita.com/tkprof/items/7d7b2d00df9c5f16fffe')"
            logger.critical(errMsg)
            raise SystemExit

        elif all(_ in excMsg for _ in ("scramble_caching_sha2", "TypeError")):
            errMsg = "please downgrade the 'PyMySQL' package (=< 0.8.1) "
            errMsg += "(Reference: 'https://github.com/PyMySQL/PyMySQL/issues/700')"
            logger.critical(errMsg)
            raise SystemExit

        elif "must be pinned buffer, not bytearray" in excMsg:
            errMsg = "error occurred at Python interpreter which "
            errMsg += "is fixed in 2.7. Please update accordingly "
            errMsg += "(Reference: 'https://bugs.python.org/issue8104')"
            logger.critical(errMsg)
            raise SystemExit

        elif all(_ in excMsg for _ in ("Resource temporarily unavailable", "os.fork()", "dictionaryAttack")):
            errMsg = "there has been a problem while running the multiprocessing hash cracking. "
            errMsg += "Please rerun with option '--threads=1'"
            logger.critical(errMsg)
            raise SystemExit

        elif "can't start new thread" in excMsg:
            errMsg = "there has been a problem while creating new thread instance. "
            errMsg += "Please make sure that you are not running too many processes"
            if not IS_WIN:
                errMsg += " (or increase the 'ulimit -u' value)"
            logger.critical(errMsg)
            raise SystemExit

        elif "can't allocate read lock" in excMsg:
            errMsg = "there has been a problem in regular socket operation "
            errMsg += "('%s')" % excMsg.strip().split('\n')[-1]
            logger.critical(errMsg)
            raise SystemExit

        elif all(_ in excMsg for _ in ("pymysql", "configparser")):
            errMsg = "wrong initialization of pymsql detected (using Python3 dependencies)"
            logger.critical(errMsg)
            raise SystemExit

        elif all(_ in excMsg for _ in ("ntlm", "socket.error, err", "SyntaxError")):
            errMsg = "wrong initialization of python-ntlm detected (using Python2 syntax)"
            logger.critical(errMsg)
            raise SystemExit

        elif all(_ in excMsg for _ in ("drda", "to_bytes")):
            errMsg = "wrong initialization of drda detected (using Python3 syntax)"
            logger.critical(errMsg)
            raise SystemExit

        elif all(_ in excMsg for _ in ("window = tkinter.Tk()",)):
            errMsg = "there has been a problem in initialization of GUI interface "
            errMsg += "('%s')" % excMsg.strip().split('\n')[-1]
            logger.critical(errMsg)
            raise SystemExit

        elif any(_ in excMsg for _ in ("unable to access item 'liveTest'",)):
            errMsg = "detected usage of files from different versions of sqlmap"
            logger.critical(errMsg)
            raise SystemExit

        elif kb.get("dumpKeyboardInterrupt"):
            raise SystemExit

        elif any(_ in excMsg for _ in ("Broken pipe",)):
            raise SystemExit

        elif valid is False:
            errMsg = "code integrity check failed (turning off automatic issue creation). "
            errMsg += "You should retrieve the latest development version from official GitHub "
            errMsg += "repository at '%s'" % GIT_PAGE
            logger.critical(errMsg)
            print()
            dataToStdout(excMsg)
            raise SystemExit

        elif any(_ in excMsg for _ in ("tamper/", "waf/")):
            logger.critical(errMsg)
            print()
            dataToStdout(excMsg)
            raise SystemExit

        elif any(_ in excMsg for _ in ("ImportError", "ModuleNotFoundError", "Can't find file for module", "SAXReaderNotAvailable", "source code string cannot contain null bytes", "No module named", "tp_name field")):
            errMsg = "invalid runtime environment ('%s')" % excMsg.split("Error: ")[-1].strip()
            logger.critical(errMsg)
            raise SystemExit

        elif all(_ in excMsg for _ in ("SyntaxError: Non-ASCII character", ".py on line", "but no encoding declared")):
            errMsg = "invalid runtime environment ('%s')" % excMsg.split("Error: ")[-1].strip()
            logger.critical(errMsg)
            raise SystemExit

        elif all(_ in excMsg for _ in ("No such file", "_'")):
            errMsg = "corrupted installation detected ('%s'). " % excMsg.strip().split('\n')[-1]
            errMsg += "You should retrieve the latest development version from official GitHub "
            errMsg += "repository at '%s'" % GIT_PAGE
            logger.critical(errMsg)
            raise SystemExit

        elif all(_ in excMsg for _ in ("HTTPNtlmAuthHandler", "'str' object has no attribute 'decode'")):
            errMsg = "package 'python-ntlm' has a known compatibility issue with the "
            errMsg += "Python 3 (Reference: 'https://github.com/mullender/python-ntlm/pull/61')"
            logger.critical(errMsg)
            raise SystemExit

        elif "'DictObject' object has no attribute '" in excMsg and all(_ in errMsg for _ in ("(fingerprinted)", "(identified)")):
            errMsg = "there has been a problem in enumeration. "
            errMsg += "Because of a considerable chance of false-positive case "
            errMsg += "you are advised to rerun with switch '--flush-session'"
            logger.critical(errMsg)
            raise SystemExit

        elif "bad marshal data (unknown type code)" in excMsg:
            match = re.search(r"\s*(.+)\s+ValueError", excMsg)
            errMsg = "one of your .pyc files are corrupted%s" % (" ('%s')" % match.group(1) if match else "")
            errMsg += ". Please delete .pyc files on your system to fix the problem"
            logger.critical(errMsg)
            raise SystemExit

        for match in re.finditer(r'File "(.+?)", line', excMsg):
            file_ = match.group(1)
            try:
                file_ = os.path.relpath(file_, os.path.dirname(__file__))
            except ValueError:
                pass
            file_ = file_.replace("\\", '/')
            if "../" in file_:
                file_ = re.sub(r"(\.\./)+", '/', file_)
            else:
                file_ = file_.lstrip('/')
            file_ = re.sub(r"/{2,}", '/', file_)
            excMsg = excMsg.replace(match.group(1), file_)

        errMsg = maskSensitiveData(errMsg)
        excMsg = maskSensitiveData(excMsg)

        if conf.get("api") or not valid:
            logger.critical("%s\n%s" % (errMsg, excMsg))
        else:
            logger.critical(errMsg)
            dataToStdout("%s\n" % setColor(excMsg.strip(), level=logging.CRITICAL))
            createGithubIssue(errMsg, excMsg)

    finally:
        kb.threadContinue = False

        if getDaysFromLastUpdate() > LAST_UPDATE_NAGGING_DAYS:
            warnMsg = "your sqlmap version is outdated"
            logger.warn(warnMsg)

        if conf.get("showTime"):
            dataToStdout("\n[*] ending @ %s\n\n" % time.strftime("%X /%Y-%m-%d/"), forceOutput=True)

        kb.threadException = True

        if kb.get("tempDir"):
            for prefix in (MKSTEMP_PREFIX.IPC, MKSTEMP_PREFIX.TESTING, MKSTEMP_PREFIX.COOKIE_JAR, MKSTEMP_PREFIX.BIG_ARRAY):
                for filepath in glob.glob(os.path.join(kb.tempDir, "%s*" % prefix)):
                    try:
                        os.remove(filepath)
                    except OSError:
                        pass

            if not filterNone(filepath for filepath in glob.glob(os.path.join(kb.tempDir, '*')) if not any(filepath.endswith(_) for _ in (".lock", ".exe", ".so", '_'))):  # ignore junk files
                try:
                    shutil.rmtree(kb.tempDir, ignore_errors=True)
                except OSError:
                    pass

        if conf.get("hashDB"):
            conf.hashDB.flush(True)

        if conf.get("harFile"):
            try:
                with openFile(conf.harFile, "w+b") as f:
                    json.dump(conf.httpCollector.obtain(), fp=f, indent=4, separators=(',', ': '))
            except SqlmapBaseException as ex:
                errMsg = getSafeExString(ex)
                logger.critical(errMsg)

        if conf.get("api"):
            conf.databaseCursor.disconnect()

        if conf.get("dumper"):
            conf.dumper.flush()

        # short delay for thread finalization
        _ = time.time()
        while threading.activeCount() > 1 and (time.time() - _) > THREAD_FINALIZATION_TIMEOUT:
            time.sleep(0.01)

        if cmdLineOptions.get("sqlmapShell"):
            cmdLineOptions.clear()
            conf.clear()
            kb.clear()
            conf.disableBanner = True
            main()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except SystemExit:
        raise
    except:
        traceback.print_exc()
    finally:
        # Reference: http://stackoverflow.com/questions/1635080/terminate-a-multi-thread-python-program
        if threading.activeCount() > 1:
            os._exit(getattr(os, "_exitcode", 0))
        else:
            sys.exit(getattr(os, "_exitcode", 0))
else:
    # cancelling postponed imports (because of Travis CI checks)
    __import__("lib.controller.controller")
