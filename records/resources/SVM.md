---
records:
    - id: SVM8HC694N
      kind: edited-volume
      title: Function Estimates
      creators:
        - name: J. S. Marron
          role: editor
      date: "1986"
      msc:
        - code: 00B25
          from: zbmath_search
        - code: 62-06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1986"
          ids:
            doi: 10.1090/conm/059
            zbl: "0596.00015"
            zbl_id: "3959311"
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "1986"
              ids:
                isbn:
                    - "9780821850626"
                    - "9780821854037"
                    - "9780821876497"
              access:
                class: record
      relations:
        - kind: part_of
          to: VAEN3CBGT1
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/conm/059
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "3959311"
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
    - id: SVMDSE7PKG
      kind: preprint
      title: Policy Learning with Weak Signals
      creators:
        - name: Benedikt Koch
          role: author
        - name: Winston Chou
          role: author
        - name: Aurélien Bibaut
          role: author
        - name: Nathan Kallus
          role: author
      date: "2026-10-07"
      subjects:
        - system: arxiv
          code: stat.ME
        - system: arxiv
          code: cs.LG
        - system: arxiv
          code: math.ST
        - system: arxiv
          code: stat.TH
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-07"
          ids:
            arxiv: "2610.10167"
      scope:
        value: border
        rule: border-arxiv
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.10167"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to border
---
