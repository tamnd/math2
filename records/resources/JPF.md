---
records:
    - id: JPF5SAMYF0
      kind: monograph
      title: 'Multigrid Methods: Proceedings of the Conference Held at Köln-Porz, November 23–27, 1981'
      creators:
        - name: W. Hackbusch
          role: editor
        - name: U. Trottenberg
          role: editor
      date: "1982"
      msc:
        - code: 00Bxx
          from: zbmath_search
        - code: 65-06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1982"
          ids:
            doi: 10.1007/bfb0069927
            zbl: "0497.00015"
            zbl_id: "3782918"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1982"
              ids:
                isbn:
                    - "9783540119555"
                    - "9783540395447"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0069927
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "3782918"
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
