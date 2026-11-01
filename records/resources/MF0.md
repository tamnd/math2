---
records:
    - id: MF0H78XZXC
      kind: preprint
      title: 'Curating Always-Loaded Context for LLM Agents: A Capacitated Assortment Model with Censored Feedback'
      creators:
        - name: Zexuan Liu
          role: author
        - name: Yuning Yang
          role: author
        - name: Tiancheng Zhao
          role: author
      date: "2026-10-07"
      subjects:
        - system: arxiv
          code: cs.AI
        - system: arxiv
          code: cs.LG
        - system: arxiv
          code: math.OC
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-07"
          ids:
            arxiv: "2610.11007"
      scope:
        value: border
        rule: border-arxiv
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.11007"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to border
    - id: MF0JK62YSM
      kind: monograph
      title: Automata on Infinite Objects and Church’s Problem
      creators:
        - name: Michael Rabin
          role: author
      date: "1972"
      msc:
        - code: 03D05
          from: zbmath_search
        - code: 68Q45
          from: zbmath_search
        - code: 03B25
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1972"
          ids:
            doi: 10.1090/cbms/013
            zbl: "0315.02037"
            zbl_id: "3492660"
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "1972"
              ids:
                isbn:
                    - "9780821816639"
                    - "9780821888629"
                    - "9781470423735"
              access:
                class: record
      relations:
        - kind: part_of
          to: 20XHFD4A67
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/cbms/013
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "3492660"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
