---
records:
    - id: QF9VEAY7XG
      kind: monograph
      title: Dirichlet Forms
      creators:
        - name: Eugene Fabes
          role: author
        - name: Masatoshi Fukushima
          role: author
        - name: Leonard Gross
          role: author
        - name: Carlos Kenig
          role: author
        - name: Michael Röckner
          role: author
        - name: Daniel W. Stroock
          role: author
        - name: Gianfausto Dell'Antonio
          role: editor
        - name: Umberto Mosco
          role: editor
      date: "1993"
      msc:
        - code: 00B25
          from: zbmath_search
        - code: 46-06
          from: zbmath_search
        - code: 31-06
          from: zbmath_search
        - code: 35-06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1993"
          ids:
            doi: 10.1007/bfb0074088
            zbl: "0782.00060"
            zbl_id: "492440"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1993"
              ids:
                isbn:
                    - "9783540574217"
                    - "9783540481515"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 dev scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0074088
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "492440"
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
          at: "2026-11-02"
          by: m2 dev scope/1
          note: from in to in
---
