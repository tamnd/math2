---
records:
    - id: 6MBZWVDYPJ
      kind: monograph
      title: 'Equadiff IV: Proceedings, Prague, August 22–26, 1977'
      creators:
        - name: Jiří Fábera
          role: editor
      date: "1979"
      msc:
        - code: 00B25
          from: zbmath_search
        - code: 34-06
          from: zbmath_search
        - code: 35-06
          from: zbmath_search
        - code: 65-06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1979"
          ids:
            doi: 10.1007/bfb0067248
            zbl: "0393.00004"
            zbl_id: "3609588"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1979"
              ids:
                isbn:
                    - "9783540091165"
                    - "9783540355199"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0067248
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "3609588"
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
