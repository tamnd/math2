---
records:
    - id: YWV2M09SS7
      kind: monograph
      title: Fonctions de Plusieurs Variables Complexes
      creators:
        - name: François Norguet
          role: editor
      date: "1974"
      msc:
        - code: 00Bxx
          from: zbmath_search
        - code: 32-06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: fr
          date: "1974"
          ids:
            doi:
                - 10.1007/bfb0068093
                - 10.1007/bfb0080242
            zbl: "0282.00015"
            zbl_id: "3442007"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1974"
              ids:
                isbn:
                    - "9783540068563"
                    - "9783540378143"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1975"
              ids:
                isbn:
                    - "9783540073970"
                    - "9783540376019"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0068093
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0080242
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "3442007"
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
