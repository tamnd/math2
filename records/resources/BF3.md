---
records:
    - id: BF36J9417A
      kind: monograph
      title: Joins and Intersections
      creators:
        - name: Hubert Flenner
          role: author
        - name: Liam O’Carroll
          role: author
        - name: Wolfgang Vogel
          role: author
      date: "1999"
      msc:
        - code: 14C17
          from: zbmath_search
        - code: 14-02
          from: zbmath_search
        - code: 13H15
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1999"
          ids:
            doi: 10.1007/978-3-662-03817-8
            zbl: "0939.14003"
            zbl_id: "1357758"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1999"
              ids:
                isbn:
                    - "9783642085628"
                    - "9783662038178"
              access:
                class: record
      relations:
        - kind: part_of
          to: FA5PXCH6G7
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-03817-8
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "1357758"
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
