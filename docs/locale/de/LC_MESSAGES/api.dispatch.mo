��          �                 B     "   P  -   s  (   �  $   �  
   �  �   �     �  (   �  &   �  "   �  ;     	   K  ?   U  �  �  I   S  ,   �  5   �  +         ,  	   L  �   V     �     
  4   '  .   \  D   �  	   �  >   �   A class representing how events become dispatched and listened to. A list of events being dispatched. Dispatches an event given out by the gateway. Keyword-only arguments of the coroutine. Multiple arguments of the coroutine. Parameters Registers a given coroutine as an event to be listened to. If the name of the event is not given, it will then be determined by the coroutine's name. Return type The coroutine event loop established on. The coroutine to register as an event. The name of the event to dispatch. The name to associate the coroutine with. Defaults to None. Variables i.e. : async def on_guild_create -> "ON_GUILD_CREATE" dispatch. Project-Id-Version: interactions.py 4.2
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2022-07-16 17:02-0400
PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE
Last-Translator: EdVraz edvraz12@gmail.com, A Python Programmer#4269 (preferred way to contact me is Discord)
Language: de
Language-Team: None
Plural-Forms: nplurals=2; plural=(n != 1)
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit
Generated-By: Babel 2.9.1
 Eine Klasse, die repräsentiert wie Events dispatched und gehört werden. Eine Liste von Events, die dispatcht werden. Dispatcht ein Event das vom Gateway ausgegeben wurde. Stichwort-begrenzte Argumente der Coroutine Mehrere Argumente der Coroutine Parameter Registriert eine gegebene Coroutine als Event auf das gehört wird. Falls der Name des Events nicht gegeben ist, wird es über den Namen der Coroutine bestimmt werden Rückgabetyp Der EventLoop der Coroutine. Die Coroutine, die als Event registriert werden soll Der name des Events, das dispatcht werden soll Der Name, der der Coroutine zugewiesen werden soll. Standard: `None` Variablen z.B.: async def on_guild_create -> "ON_GUILD_CREATE" dispatch. 